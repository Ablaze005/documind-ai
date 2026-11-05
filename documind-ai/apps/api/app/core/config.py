from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DocuMind AI"
    app_env: str = "development"
    api_v1_prefix: str = "/api/v1"
    app_port: int = 8000
    app_secret_key: str = "change-me"
    postgres_url: str = "postgresql://documind:documind@localhost:5432/documind"
    redis_url: str = "redis://localhost:6379/0"
    openai_api_key: str = ""
    groq_api_key: str = ""
    gemini_api_key: str = ""
    ollama_base_url: str = "http://localhost:11434"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
