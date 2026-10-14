import json
import urllib.error
import urllib.request

from groq import Groq
from dataforge.config_manager import get_config


def _post_json(url, payload, headers=None, timeout=60):
    request_headers = {"Content-Type": "application/json"}
    request_headers.update(headers or {})
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=request_headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def ask_enterprise_ai(prompt):
    """Route a prompt to the provider selected in ~/.dataforge/config.json."""
    config = get_config() or {}
    provider = str(config.get("ai_provider", config.get("provider", "groq"))).strip().lower()
    api_key = config.get(f"{provider}_api_key") or config.get("api_key")

    if provider == "ollama":
        model = config.get("ollama_model", "llama3")
        try:
            result = _post_json(
                config.get("ollama_url", "http://localhost:11434/api/generate"),
                {"model": model, "prompt": prompt, "stream": False},
                timeout=60,
            )
        except Exception as exc:
            raise RuntimeError(
                "Could not connect to Ollama. Start Ollama and verify the configured model."
            ) from exc
        answer = result.get("response")
        if not answer:
            raise RuntimeError("Ollama returned an empty response.")
        return answer

    if not api_key:
        raise ValueError(
            f"Missing API key for {provider}. Run 'python main.py setup' and configure credentials."
        )

    if provider == "groq":
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=config.get("groq_model", "llama-3.3-70b-versatile"),
        )
        return completion.choices[0].message.content

    if provider == "openai":
        result = _post_json(
            "https://api.openai.com/v1/chat/completions",
            {
                "model": config.get("openai_model", "gpt-4o-mini"),
                "messages": [{"role": "user", "content": prompt}],
            },
            {"Authorization": f"Bearer {api_key}"},
        )
        try:
            return result["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError("OpenAI returned an unexpected response format.") from exc

    if provider == "gemini":
        url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            + config.get("gemini_model", "gemini-2.5-flash")
            + ":generateContent?key="
            + urllib.parse.quote(api_key, safe="")
        )
        result = _post_json(
            url,
            {"contents": [{"parts": [{"text": prompt}]}]},
        )
        try:
            return "".join(part["text"] for part in result["candidates"][0]["content"]["parts"])
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError("Gemini returned an unexpected response format.") from exc

    if provider == "claude":
        result = _post_json(
            "https://api.anthropic.com/v1/messages",
            {
                "model": config.get("claude_model", "claude-3-5-haiku-latest"),
                "max_tokens": 4096,
                "messages": [{"role": "user", "content": prompt}],
            },
            {
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
        )
        try:
            return "".join(
                block["text"] for block in result["content"] if block.get("type") == "text"
            )
        except (KeyError, TypeError) as exc:
            raise RuntimeError("Claude returned an unexpected response format.") from exc

    raise ValueError(
        f"Unsupported AI provider '{provider}'. Supported providers: groq, openai, gemini, claude, ollama."
    )


def ask_groq(prompt, api_key=None):
    """Backward-compatible alias; routing follows the configured provider."""
    return ask_enterprise_ai(prompt)
