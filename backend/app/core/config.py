from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "LinguaQuest API"
    openai_api_key: str
    elevenlabs_api_key: str
    elevenlabs_base_url: str = "https://api.elevenlabs.io/v1"
    audio_cdn_base_url: str = "https://cdn.example.com/audio"


settings = Settings()
