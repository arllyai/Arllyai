import hashlib
from dataclasses import dataclass

import httpx

from app.core.config import settings


SUPPORTED_LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "pt": "Portuguese",
    "zh-CN": "Chinese (Simplified)",
    "zh-TW": "Chinese (Traditional)",
    "vi": "Vietnamese",
    "ja": "Japanese",
    "ko": "Korean",
    "it": "Italian",
    "ar": "Arabic",
}


@dataclass
class VoiceRequest:
    text: str
    language: str
    voice_id: str | None = None
    model_id: str = "eleven_multilingual_v2"
    stability: float = 0.4
    similarity_boost: float = 0.8


class ElevenLabsService:
    """ElevenLabs integration layer with cache keys and key rotation."""

    def _select_voice(self, req: VoiceRequest) -> str:
        if req.voice_id:
            return req.voice_id

        voice = settings.language_voice_map.get(req.language)
        if not voice:
            raise ValueError(f"Unsupported language '{req.language}'.")
        return voice

    def _cache_key(self, req: VoiceRequest, voice_id: str) -> str:
        raw = f"{req.text}|{req.language}|{voice_id}|{req.model_id}|{req.stability}|{req.similarity_boost}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    async def synthesize(self, req: VoiceRequest) -> tuple[str, bytes]:
        voice_id = self._select_voice(req)
        cache_key = self._cache_key(req, voice_id)
        payload = {
            "text": req.text,
            "model_id": req.model_id,
            "voice_settings": {
                "stability": req.stability,
                "similarity_boost": req.similarity_boost,
            },
        }

        errors: list[str] = []
        for key in settings.active_elevenlabs_keys:
            headers = {
                "xi-api-key": key,
                "accept": "audio/mpeg",
                "content-type": "application/json",
            }
            url = f"{settings.elevenlabs_base_url}/text-to-speech/{voice_id}"

            async with httpx.AsyncClient(timeout=30) as client:
                res = await client.post(url, headers=headers, json=payload)

            if res.is_success:
                audio_bytes = res.content
                asset_url = f"{settings.audio_cdn_base_url}/{cache_key}.mp3"
                return asset_url, audio_bytes

            errors.append(f"{res.status_code}:{res.text[:80]}")

        raise RuntimeError(f"ElevenLabs synthesis failed across configured keys: {errors}")

    async def score_pronunciation(self, target_text: str, spoken_text: str) -> dict[str, float | str]:
        """Lightweight placeholder scoring (replace with Whisper/phoneme scorer in production)."""
        target_words = target_text.lower().split()
        spoken_words = spoken_text.lower().split()

        if not target_words:
            return {"score": 0.0, "feedback": "Target text missing."}

        overlap = len(set(target_words).intersection(set(spoken_words)))
        score = round((overlap / max(len(target_words), 1)) * 100, 2)

        if score >= 85:
            feedback = "Great pronunciation and word coverage."
        elif score >= 60:
            feedback = "Good attempt. Focus on missing words and rhythm."
        else:
            feedback = "Try again slowly and match each word clearly."

        return {"score": score, "feedback": feedback}
