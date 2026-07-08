#!/usr/bin/env bun
/**
 * zo-mcp-bridge-stdio.js
 * MCP bridge using stdio transport (JSON-RPC 2.0 over stdin/stdout)
 * Compatible with OpenClaw MCP server integration
 */
"use strict";

const ZO_API_URL = "https://api.zo.computer/mcp";
const AUTH_TOKEN = process.env.ZO_CLIENT_IDENTITY_TOKEN;

if (!AUTH_TOKEN) {
  process.stderr.write("❌ ZO_CLIENT_IDENTITY_TOKEN not set\n");
  process.exit(1);
}

let toolCache = [];

async function callZoTool(toolName, args) {
  const body = {
    jsonrpc: "2.0",
    method: "tools/call",
    id: Math.random().toString(36).slice(2),
    params: { name: toolName, arguments: args },
  };

  const resp = await fetch(ZO_API_URL, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${AUTH_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });

  if (!resp.ok) throw new Error(`Zo API error: ${resp.status}`);
  const result = await resp.json();
  if (result.error) throw new Error(result.error.message || JSON.stringify(result.error));
  return result.result;
}

async function listZoTools() {
  const body = {
    jsonrpc: "2.0",
    method: "tools/list",
    id: Math.random().toString(36).slice(2),
    params: {},
  };

  const resp = await fetch(ZO_API_URL, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${AUTH_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });

  if (!resp.ok) throw new Error(`List tools failed: ${resp.status}`);
  const result = await resp.json();
  return result.result?.tools || [];
}

// MCP Protocol: JSON-RPC 2.0 messages delimited by newlines on stdin/stdout
async function sendResponse(id, result) {
  const msg = JSON.stringify({ jsonrpc: "2.0", id, result });
  process.stdout.write(msg + "\n");
}

async function sendError(id, code, message) {
  const msg = JSON.stringify({ jsonrpc: "2.0", id, error: { code, message } });
  process.stdout.write(msg + "\n");
}

async function handleMessage(msg) {
  try {
    const { id, method, params } = msg;

    if (method === "initialize") {
      await sendResponse(id, {
        protocolVersion: "2024-11-05",
        capabilities: { tools: {} },
        serverInfo: { name: "zo-mcp-bridge", version: "1.0.0" },
      });
      return;
    }

    if (method === "tools/list") {
      await sendResponse(id, {
        tools: toolCache.map((t) => ({
          name: t.name,
          description: t.description || `Zo tool: ${t.name}`,
          inputSchema: t.inputSchema || { type: "object", properties: {} },
        })),
      });
      return;
    }

    if (method === "tools/call") {
      try {
        const result = await callZoTool(params.name, params.arguments || {});
        await sendResponse(id, result);
      } catch (err) {
        await sendError(id, -32603, err.message);
      }
      return;
    }

    // Notifcations (no id) — don't respond
    if (id === undefined) return;

    await sendError(id, -32601, "Method not found");
  } catch (err) {
    await sendError(msg.id || null, -32603, err.message);
  }
}

async function main() {
  try {
    toolCache = await listZoTools();
    process.stderr.write(`🔌 Zo MCP Bridge (stdio) — ${toolCache.length} tools loaded\n`);
  } catch (err) {
    process.stderr.write(`❌ Failed to load tools: ${err.message}\n`);
    process.exit(1);
  }

  let buffer = "";
  process.stdin.setEncoding("utf8");
  process.stdin.on("data", (chunk) => {
    buffer += chunk;
    while (buffer.includes("\n")) {
      const idx = buffer.indexOf("\n");
      const line = buffer.slice(0, idx);
      buffer = buffer.slice(idx + 1);
      if (line.trim()) {
        try {
          const msg = JSON.parse(line);
          handleMessage(msg);
        } catch (e) {
          // ignore parse errors on individual messages
        }
      }
    }
  });

  process.stdin.on("end", () => process.exit(0));
}

main();
