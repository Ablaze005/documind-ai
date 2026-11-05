# DocuMind AI architecture

## Overview

DocuMind AI combines repository analysis, AI synthesis, and dashboard presentation to turn repository metadata into polished developer docs.

## Components

### 1. Frontend dashboard

The Next.js frontend provides a single interface for repository URL entry, generation triggers, status feedback, and output preview.

### 2. FastAPI backend

The backend exposes versioned endpoints under `/api/v1` and orchestrates analysis workflows, service calls, and output processing.

### 3. Repository analyzer

This module clones repositories and inspects files for languages, frameworks, functions, classes, and structure.

### 4. AI engine

The AI layer abstracts providers such as OpenAI, Groq, Gemini, and Ollama behind a common `generate(prompt)` contract.

### 5. Documentation generator

The documentation package turns repository metadata into README docs, architecture notes, and project summaries.

## Execution flow

1. User enters a GitHub URL in the dashboard.
2. API validates the request and triggers the repository analysis service.
3. Analyzer inspects the repository and returns metadata.
4. AI engine synthesizes summary text and key explanations.
5. Documentation generator assembles markdown bundles.
6. UI presents the final output and enables downloads.
