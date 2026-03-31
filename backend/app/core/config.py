import json
from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


DEFAULT_LANGUAGE_VOICE_MAP: dict[str, str] = {
    "en": "voice_english_default",
    "es": "voice_spanish_default",
    "fr": "voice_french_default",
    "pt": "voice_portuguese_default",
    "zh-CN": "voice_chinese_simplified_default",
    "zh-TW": "voice_chinese_traditional_default",
    "vi": "voice_vietnamese_default",
    "ja": "voice_japanese_default",
    "ko": "voice_korean_default",
    "it": "voice_italian_default",
    "ar": "voice_arabic_default",
}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "LinguaQuest API"

    # OpenAI and speech model keys
    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")

    # ElevenLabs: allow primary + backup keys for rotation/failover
    elevenlabs_api_key_primary: str = Field(default="", alias="ELEVENLABS_API_KEY_PRIMARY")
    elevenlabs_api_key_backup: str = Field(default="", alias="ELEVENLABS_API_KEY_BACKUP")
    elevenlabs_api_key_recording: str = Field(default="", alias="ELEVENLABS_API_KEY_RECORDING")

    elevenlabs_base_url: str = Field(default="https://api.elevenlabs.io/v1", alias="ELEVENLABS_BASE_URL")
    audio_cdn_base_url: str = Field(default="https://cdn.example.com/audio", alias="AUDIO_CDN_BASE_URL")

    # JSON string env var, e.g. {"en":"...","es":"..."}
    language_voice_map_json: str = Field(default="", alias="ELEVENLABS_LANGUAGE_VOICE_MAP_JSON")

    @property
    def active_elevenlabs_keys(self) -> list[str]:
        return [
            key
            for key in [
                self.elevenlabs_api_key_primary,
                self.elevenlabs_api_key_backup,
                self.elevenlabs_api_key_recording,
            ]
            if key
        ]

    @property
    def language_voice_map(self) -> dict[str, str]:
        if not self.language_voice_map_json:
            return DEFAULT_LANGUAGE_VOICE_MAP

        try:
            parsed: Any = json.loads(self.language_voice_map_json)
        except json.JSONDecodeError:
            return DEFAULT_LANGUAGE_VOICE_MAP

        if not isinstance(parsed, dict):
            return DEFAULT_LANGUAGE_VOICE_MAP

        merged = DEFAULT_LANGUAGE_VOICE_MAP.copy()
        merged.update({str(k): str(v) for k, v in parsed.items()})
        return merged


settings = Settings()
