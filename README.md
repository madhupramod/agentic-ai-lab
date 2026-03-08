# Agentic AI Lab

**By Madhu Pramod Adithya**

Hands-on projects exploring AI agent patterns — tool use, multi-agent orchestration, and autonomous workflows — built with CrewAI, LangGraph, AutoGen, and MCP using local models via Ollama.

Inspired by concepts from [Ed Donner's Complete Agentic AI Engineering Course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course). All projects are original implementations using my own problem domains and local-first tooling.

## Structure

| Week | Topic          | Project | Status |
| ---- | -------------- | ------- | ------ |
| 1    | Foundations    |         | 🔲     |
| 2    | Agent Patterns |         | 🔲     |
| 3    | CrewAI         |         | 🔲     |
| 4    | LangGraph      |         | 🔲     |
| 5    | AutoGen        |         | 🔲     |
| 6    | MCP            |         | 🔲     |

## Toolkit

- **Code editor:** VS Code
- **Autocomplete:** Qwen 2.5 Coder 1.5B via Ollama + Continue extension
- **Local LLM (code):** Qwen 2.5 Coder 14B via Ollama
- **Local LLM (chat):** Qwen 2.5 14B via Ollama + Continue extension
- **Python:** 3.14 via uv

All LLM inference runs locally. No API keys required to run the projects.

## Setup

Prerequisites: [Ollama](https://ollama.com), [uv](https://docs.astral.sh/uv/), and Git.

```bash
# Clone and install
git clone https://github.com/madhupramod/agentic-ai-lab.git
cd agentic-ai-lab
uv sync

# Pull the local models
ollama pull qwen2.5-coder:1.5b    # autocomplete
ollama pull qwen2.5:14b            # chat
ollama pull qwen2.5-coder:14b      # code execution in notebooks
```

Then open the project in VS Code and select the `.venv (Python 3.14)` kernel for notebooks.

## Running a Notebook

```python
from shared.utils import chat

response = chat("Explain the ReAct pattern for AI agents.")
print(response)
```

Everything routes through Ollama locally — no cloud calls, no keys, no cost.

## Key Learnings

_Updated as I progress through the course._

## Commits

This project uses [Conventional Commits](https://www.conventionalcommits.org/).

## License

MIT
