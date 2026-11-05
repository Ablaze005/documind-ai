from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    name: str

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class OpenAIProvider(BaseProvider):
    name = "openai"

    def generate(self, prompt: str) -> str:
        return f"[OpenAI] Summary for: {prompt[:80]}"


class GroqProvider(BaseProvider):
    name = "groq"

    def generate(self, prompt: str) -> str:
        return f"[Groq] Summary for: {prompt[:80]}"


class GeminiProvider(BaseProvider):
    name = "gemini"

    def generate(self, prompt: str) -> str:
        return f"[Gemini] Summary for: {prompt[:80]}"


class OllamaProvider(BaseProvider):
    name = "ollama"

    def generate(self, prompt: str) -> str:
        return f"[Ollama] Summary for: {prompt[:80]}"


class ProviderFactory:
    registry = {
        "openai": OpenAIProvider,
        "groq": GroqProvider,
        "gemini": GeminiProvider,
        "ollama": OllamaProvider,
    }

    @classmethod
    def create(cls, provider_name: str) -> BaseProvider:
        provider_cls = cls.registry.get(provider_name.lower())
        if provider_cls is None:
            raise ValueError(f"Unsupported provider: {provider_name}")
        return provider_cls()
