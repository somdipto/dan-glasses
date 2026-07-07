#!/usr/bin/env bun
/**
 * zo-mcp-bridge.js
 * Bridges OpenClaw tool calls to Zo MCP API
 * 
 * Registers Zo tools as OpenClaw tools → proxies calls via direct HTTP POST
 */

const ZO_API_URL = "https://api.zo.computer/mcp";
const AUTH_TOKEN = process.env.ZO_CLIENT_IDENTITY_TOKEN;

if (!AUTH_TOKEN) {
  console.error("❌ ZO_CLIENT_IDENTITY_TOKEN not set");
  process.exit(1);
}

const TOOL_CACHE = new Map();
const START_TS = Date.now();

async function callZoTool(toolName, args) {
  const body = {
    jsonrpc: "2.0",
    method: "tools/call",
    id: Math.random().toString(36).slice(2),
    params: {
      name: toolName,
      arguments: args,
    },
  };

  const resp = await fetch(ZO_API_URL, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${AUTH_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });

  if (!resp.ok) {
    throw new Error(`Zo API error: ${resp.status} ${resp.statusText}`);
  }

  const result = await resp.json();
  
  if (result.error) {
    throw new Error(`Tool error: ${result.error.message || JSON.stringify(result.error)}`);
  }
  
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

async function main() {
  console.log("🔌 Zo MCP Bridge starting...");
  
  try {
    // Fetch and cache tool list
    const tools = await listZoTools();
    console.log(`📋 Cached ${tools.length} Zo tools`);
    
    for (const tool of tools) {
      TOOL_CACHE.set(tool.name, tool);
    }
    
    // Start the MCP bridge server on a high port
    const port = parseInt(process.env.BRIDGE_PORT || "18790");
    
    const server = Bun.serve({
      port,
      async fetch(req) {
        const url = new URL(req.url);

        // Liveness probe for supervisor / external health checks.
        if (url.pathname === "/healthz" || url.pathname === "/health") {
          return Response.json({
            ok: true,
            service: "zo-mcp-bridge",
            tools_cached: TOOL_CACHE.size,
            uptime_ms: Date.now() - START_TS,
          });
        }

        try {
          const body = await req.json();
          
          if (body.method === "tools/list") {
            return Response.json({
              jsonrpc: "2.0",
              id: body.id,
              result: { tools: tools.map(t => ({
                name: t.name,
                description: t.description || `Zo tool: ${t.name}`,
                inputSchema: t.inputSchema || { type: "object", properties: {} }
              })) }
            });
          }
          
          if (body.method === "tools/call") {
            const toolName = body.params?.name;
            const args = body.params?.arguments || {};
            
            console.log(`🔧 Calling Zo tool: ${toolName}`);
            const result = await callZoTool(toolName, args);
            
            return Response.json({
              jsonrpc: "2.0",
              id: body.id,
              result
            });
          }
          
          if (body.method === "initialize") {
            return Response.json({
              jsonrpc: "2.0",
              id: body.id,
              result: {
                protocolVersion: "2024-11-05",
                capabilities: { tools: {} },
                serverInfo: { name: "zo-mcp-bridge", version: "1.0.0" }
              }
            });
          }
          
          return Response.json({
            jsonrpc: "2.0",
            id: body.id,
            error: { code: -32601, message: "Method not found" }
          });
        } catch (err) {
          console.error("Bridge error:", err);
          return Response.json({
            jsonrpc: "2.0",
            id: null,
            error: { code: -32603, message: err.message }
          }, { status: 500 });
        }
      }
    });
    
    console.log(`✅ Zo MCP Bridge running on port ${port}`);
    console.log(`   Tools: ${tools.length} available`);
    console.log(`   Endpoint: http://localhost:${port}`);
    
  } catch (err) {
    console.error("❌ Bridge failed to start:", err.message);
    process.exit(1);
  }
}

main();