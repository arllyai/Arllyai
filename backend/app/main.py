from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.services.ai_tutor import SYSTEM_PROMPT, SUPPORTED_TUTOR_LANGUAGES, build_user_prompt
from app.services.elevenlabs_service import ElevenLabsService, SUPPORTED_LANGUAGES, VoiceRequest

app = FastAPI(title="LinguaQuest API", version="0.2.0")
voice_service = ElevenLabsService()


class TTSBody(BaseModel):
    text: str
    language: str = Field(description="Target language code, e.g. en, es, zh-CN")
    voice_id: str | None = None
    model_id: str = "eleven_multilingual_v2"


class PronunciationBody(BaseModel):
    language: str
    target_text: str
    spoken_text: str


class TutorBody(BaseModel):
    mode: str = Field(default="grammar", description="speaking | writing | grammar")
    learner_text: str
    target_language: str
    native_language: str
    cefr_level: str = "A1"
    error_tags: list[str] = []


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/v1/voice/languages")
async def voice_languages() -> dict[str, dict[str, str]]:
    return {"supported_languages": SUPPORTED_LANGUAGES}


@app.post("/v1/voice/tts")
async def tts(body: TTSBody) -> dict[str, str]:
    if body.language not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Unsupported language: {body.language}")

    asset_url, _audio_bytes = await voice_service.synthesize(
        VoiceRequest(
            text=body.text,
            language=body.language,
            voice_id=body.voice_id,
            model_id=body.model_id,
        )
    )
    return {"audio_url": asset_url}


@app.post("/v1/voice/pronunciation/score")
async def pronunciation_score(body: PronunciationBody) -> dict[str, float | str]:
    if body.language not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Unsupported language: {body.language}")
    return await voice_service.score_pronunciation(body.target_text, body.spoken_text)


@app.post("/v1/tutor/assist")
async def tutor_assist(body: TutorBody) -> dict[str, str]:
    if body.target_language not in SUPPORTED_TUTOR_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Unsupported language: {body.target_language}")
    if body.mode not in {"speaking", "writing", "grammar"}:
        raise HTTPException(status_code=400, detail=f"Unsupported mode: {body.mode}")

    user_prompt = build_user_prompt(
        mode=body.mode,
        target_language=body.target_language,
        native_language=body.native_language,
        learner_text=body.learner_text,
        error_tags=body.error_tags,
        cefr_level=body.cefr_level,
    )
    return {"system_prompt": SYSTEM_PROMPT, "user_prompt": user_prompt}
