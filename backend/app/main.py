from fastapi import FastAPI
from pydantic import BaseModel

from app.services.ai_tutor import SYSTEM_PROMPT, build_user_prompt
from app.services.elevenlabs_service import ElevenLabsService, VoiceRequest

app = FastAPI(title="LinguaQuest API", version="0.1.0")
voice_service = ElevenLabsService()


class TTSBody(BaseModel):
    text: str
    voice_id: str
    model_id: str = "eleven_multilingual_v2"


class TutorBody(BaseModel):
    learner_text: str
    target_language: str
    native_language: str
    cefr_level: str = "A1"
    error_tags: list[str] = []


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/voice/tts")
async def tts(body: TTSBody) -> dict[str, str]:
    asset_url, _audio_bytes = await voice_service.synthesize(
        VoiceRequest(text=body.text, voice_id=body.voice_id, model_id=body.model_id)
    )
    return {"audio_url": asset_url}


@app.post("/v1/tutor/prompt-preview")
async def tutor_prompt_preview(body: TutorBody) -> dict[str, str]:
    user_prompt = build_user_prompt(
        target_language=body.target_language,
        native_language=body.native_language,
        learner_text=body.learner_text,
        error_tags=body.error_tags,
        cefr_level=body.cefr_level,
    )
    return {"system_prompt": SYSTEM_PROMPT, "user_prompt": user_prompt}
