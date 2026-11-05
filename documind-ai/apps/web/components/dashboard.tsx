'use client';

import { useMemo, useState } from 'react';
import { Download, GitBranch, Sparkles, CheckCircle2, ArrowRight } from 'lucide-react';

const sampleDoc = `# Example Project

## Overview
This repository is a Python API for automating documentation generation.

## Architecture
- API layer exposes analysis endpoints
- Repository analyzer scans files and extracts metadata
- AI layer synthesizes summaries and overviews

## Setup
1. Clone the repo
2. Create a virtual environment
3. Install dependencies
4. Start the FastAPI app

## Contributing
Please open a feature branch and share a clear pull request summary.
`;

export function Dashboard() {
  const [url, setUrl] = useState('https://github.com/openai/openai-python');
  const [status, setStatus] = useState<'idle' | 'running' | 'done'>('idle');
  const [result, setResult] = useState({
    repository: 'openai-python',
    language: 'Python',
    framework: 'FastAPI',
    files: 124,
    functions: 89,
    classes: 15,
    summary: sampleDoc
  });

  const stats = useMemo(
    () => [
      { label: 'Languages', value: result.language },
      { label: 'Framework', value: result.framework },
      { label: 'Files', value: String(result.files) },
      { label: 'Functions', value: String(result.functions) }
    ],
    [result]
  );

  async function handleGenerate() {
    setStatus('running');

    await new Promise((resolve) => setTimeout(resolve, 1200));
    setResult({
      repository: url.split('/').filter(Boolean).pop() ?? 'repository',
      language: 'Python',
      framework: 'FastAPI',
      files: 132,
      functions: 101,
      classes: 18,
      summary: sampleDoc
    });
    setStatus('done');
  }

  return (
    <main className="min-h-screen px-6 py-10 text-slate-50">
      <div className="mx-auto max-w-7xl">
        <header className="mb-8 flex items-center justify-between">
          <div>
            <p className="mb-2 inline-flex items-center gap-2 rounded-full border border-sky-500/30 bg-sky-500/10 px-3 py-1 text-xs font-medium uppercase tracking-[0.2em] text-sky-300">
              <Sparkles className="h-3.5 w-3.5" />
              AI Repository Intelligence
            </p>
            <h1 className="text-3xl font-bold tracking-tight">DocuMind AI Dashboard</h1>
          </div>
          <div className="rounded-full border border-emerald-500/30 bg-emerald-500/10 px-3 py-1.5 text-sm text-emerald-300">
            {status === 'done' ? 'Analysis complete' : status === 'running' ? 'Generating documentation...' : 'Ready to analyze'}
          </div>
        </header>

        <section className="grid gap-6 lg:grid-cols-[1.2fr_2fr]">
          <div className="rounded-2xl border border-slate-800 bg-slate-900/60 p-6 shadow-glow">
            <div className="mb-5 flex items-center gap-2 text-sm font-medium text-slate-300">
              <GitBranch className="h-4 w-4 text-sky-400" />
              Repository URL
            </div>

            <input
              value={url}
              onChange={(event) => setUrl(event.target.value)}
              placeholder="https://github.com/owner/repository"
              className="w-full rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-sm text-slate-100 outline-none ring-0 placeholder:text-slate-500"
            />

            <button
              onClick={handleGenerate}
              className="mt-5 inline-flex w-full items-center justify-center gap-2 rounded-xl bg-sky-500 px-4 py-3 font-medium text-white transition hover:bg-sky-400 disabled:opacity-70"
              disabled={status === 'running'}
            >
              {status === 'running' ? 'Analyzing...' : 'Generate Documentation'}
              <ArrowRight className="h-4 w-4" />
            </button>

            <div className="mt-6 space-y-3">
              {stats.map((stat) => (
                <div key={stat.label} className="flex items-center justify-between rounded-xl border border-slate-800 bg-slate-950/60 px-4 py-3">
                  <span className="text-sm text-slate-400">{stat.label}</span>
                  <span className="text-sm font-semibold text-slate-100">{stat.value}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-2xl border border-slate-800 bg-slate-900/60 p-6 shadow-glow">
            <div className="mb-4 flex items-center justify-between">
              <div>
                <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Generated output</p>
                <h2 className="mt-2 text-2xl font-semibold text-white">{result.repository}</h2>
              </div>
              <button className="inline-flex items-center gap-2 rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm text-slate-200">
                <Download className="h-4 w-4" />
                Download
              </button>
            </div>

            <div className="mb-5 flex items-center gap-2 rounded-lg border border-emerald-500/20 bg-emerald-500/5 px-3 py-2 text-sm text-emerald-300">
              <CheckCircle2 className="h-4 w-4" />
              Documentation generated for {result.repository}
            </div>

            <pre className="max-h-[28rem] overflow-auto whitespace-pre-wrap rounded-xl border border-slate-800 bg-slate-950 p-4 text-sm leading-7 text-slate-200">
              {result.summary}
            </pre>
          </div>
        </section>
      </div>
    </main>
  );
}
