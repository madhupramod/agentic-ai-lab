"""
Shared LLM utilities — defaults to local Ollama. No API keys needed.

Uses the code-specialised model for notebook execution (better at
generating and reasoning about code than the general-purpose model).

Usage:
    from shared.utils import chat
    response = chat("Explain agentic AI in three sentences.")
"""

from openai import OpenAI

# Code-specialised model for notebooks — change size to match your RAM
DEFAULT_MODEL = "qwen2.5-coder:14b"


def get_client():
    """Return an OpenAI-compatible client pointing at local Ollama."""
    return OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


def chat(prompt, system=None, model=None):
    """Single-turn chat via local Ollama. No API key required."""
    model = model or DEFAULT_MODEL
    client = get_client()
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


def chat_stream(prompt, system=None, model=None):
    """Streaming chat via local Ollama. Prints tokens as they arrive."""
    model = model or DEFAULT_MODEL
    client = get_client()
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    stream = client.chat.completions.create(
        model=model, messages=messages, stream=True
    )
    result = []
    for chunk in stream:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            print(token, end="", flush=True)
            result.append(token)
    print()
    return "".join(result)


def list_models():
    """Show which models are available in Ollama."""
    import subprocess
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    print(result.stdout)