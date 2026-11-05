# DocuMind AI

DocuMind AI is an AI-powered repository intelligence platform that analyzes GitHub repositories and automatically generates developer-friendly documentation.

## Features

- Accept a GitHub repository URL
- Clone and analyze repositories locally
- Detect languages, frameworks, files, classes, and functions
- Generate README, architecture, and project summaries
- Preview generated output in a dashboard UI
- Download generated documentation
- Support multiple AI providers: OpenAI, Groq, Gemini, and Ollama

## Tech Stack

- Frontend: Next.js 15, TypeScript, Tailwind CSS, Shadcn UI
- Backend: FastAPI, Python 3.12
- AI Providers: OpenAI, Groq, Gemini, Ollama
- Repository Analysis: GitPython, Tree-Sitter, AST parsing, Git CLI
- Storage: PostgreSQL, Redis
- Containerization: Docker, Docker Compose

## Project Structure

```text
DocuMind AI/
├─ apps/
│  ├─ web/
│  └─ api/
├─ packages/
│  ├─ repo-analyzer/
│  ├─ doc-generator/
│  ├─ ai-engine/
│  ├─ prompts/
│  └─ shared/
├─ data/
├─ docs/
├─ tests/
├─ scripts/
├─ .github/
├─ docker-compose.yml
├─ .env.example
├─ README.md
└─ package.json
```

## Quick Start

### 1. Start infrastructure

```bash
docker compose up -d postgres redis
```

### 2. Start the API

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 3. Start the web app

```bash
cd apps/web
npm install
npm run dev
```

Visit http://localhost:3000 to access the dashboard.

## MVP Scope

This repository provides an initial implementation for the MVP:

- FastAPI backend with router-driven architecture
- Next.js dashboard with repository form and preview panel
- Repository analysis engine with metadata extraction
- AI provider abstraction for multiple models
- Documentation generator for README and architecture overview
- Unit tests for API and analyzer logic

## License

MIT
