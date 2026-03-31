import hashlib
from dataclasses import dataclass

import httpx

from app.core.config import settings


@dataclass
class VoiceRequest:
    text: str
    voice_id: str
    model_id: str = "eleven_multilingual_v2"
    stability: float = 0.4
    similarity_boost: float = 0.8


class ElevenLabsService:
    """ElevenLabs integration layer with deterministic cache keys."""

    def _cache_key(self, req: VoiceRequest) -> str:
        raw = f"{req.text}|{req.voice_id}|{req.model_id}|{req.stability}|{req.similarity_boost}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    async def synthesize(self, req: VoiceRequest) -> tuple[str, bytes]:
        cache_key = self._cache_key(req)
        # 1) Try Redis/S3 lookup using cache_key (omitted infra adapter for brevity)

        payload = {
            "text": req.text,
            "model_id": req.model_id,
            "voice_settings": {
                "stability": req.stability,
                "similarity_boost": req.similarity_boost,
            },
        }
        headers = {
            "xi-api-key": settings.elevenlabs_api_key,
            "accept": "audio/mpeg",
            "content-type": "application/json",
        }
        url = f"{settings.elevenlabs_base_url}/text-to-speech/{req.voice_id}"

        async with httpx.AsyncClient(timeout=30) as client:
            res = await client.post(url, headers=headers, json=payload)
            res.raise_for_status()
            audio_bytes = res.content

        # 2) Persist bytes to object storage and return stable URL (adapter omitted)
        asset_url = f"{settings.audio_cdn_base_url}/{cache_key}.mp3"
        return asset_url, audio_bytes
