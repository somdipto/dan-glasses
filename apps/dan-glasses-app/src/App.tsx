import { useState } from 'react';
import BootstrapWizard from './components/BootstrapWizard';
import LiveTranscript from './components/LiveTranscript';
import TtsPanel from './components/TtsPanel';
import MemoryPanel from './components/MemoryPanel';
import VisionDashboard from './components/VisionDashboard';

type Tab = 'wizard' | 'vision' | 'memory' | 'tts' | 'transcript';

export default function App() {
  const [tab, setTab] = useState<Tab>('wizard');

  return (
    <div className="dan-glasses-app">
      <nav className="app-tabs">
        <button type="button" className={tab === 'wizard' ? 'tab active' : 'tab'} onClick={() => setTab('wizard')}>
          Bootstrap
        </button>
        <button type="button" className={tab === 'vision' ? 'tab active' : 'tab'} onClick={() => setTab('vision')}>
          Vision
        </button>
        <button type="button" className={tab === 'memory' ? 'tab active' : 'tab'} onClick={() => setTab('memory')}>
          Memory
        </button>
        <button type="button" className={tab === 'tts' ? 'tab active' : 'tab'} onClick={() => setTab('tts')}>
          TTS
        </button>
        <button type="button" className={tab === 'transcript' ? 'tab active' : 'tab'} onClick={() => setTab('transcript')}>
          Live
        </button>
      </nav>
      <main className="app-main">
        {tab === 'wizard' && <BootstrapWizard />}
        {tab === 'vision' && <VisionDashboard />}
        {tab === 'memory' && <MemoryPanel />}
        {tab === 'tts' && <TtsPanel />}
        {tab === 'transcript' && <LiveTranscript wsPort={8091} />}
      </main>
    </div>
  );
}
