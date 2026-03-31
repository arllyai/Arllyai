# LinguaQuest AI

Production-ready blueprint for an AI-powered language learning platform inspired by Duolingo, with:

- Gamified progression (XP, streaks, hearts, badges, leaderboards)
- Adaptive lessons (vocabulary, grammar, listening, speaking)
- AI tutor powered by LLMs for personalized explanations and conversation
- Real-time voice support using ElevenLabs TTS + pronunciation scoring

## Stack

- **Frontend**: Next.js + Tailwind CSS (mobile-first)
- **Backend**: FastAPI (Python)
- **DB**: PostgreSQL
- **AI**: OpenAI API (exercise generation, tutor, personalization)
- **Voice**: ElevenLabs API
- **Infra**: Redis cache, S3-compatible blob storage, background workers

## ElevenLabs API Key Setup (secure)

> Keys are configured via environment variables, not hardcoded in source.

```bash
OPENAI_API_KEY=...
ELEVENLABS_API_KEY_PRIMARY=...
ELEVENLABS_API_KEY_BACKUP=...
ELEVENLABS_API_KEY_RECORDING=...
ELEVENLABS_LANGUAGE_VOICE_MAP_JSON='{"en":"voice_id_en","es":"voice_id_es","fr":"voice_id_fr","pt":"voice_id_pt","zh-CN":"voice_id_zh_cn","zh-TW":"voice_id_zh_tw","vi":"voice_id_vi","ja":"voice_id_ja","ko":"voice_id_ko","it":"voice_id_it","ar":"voice_id_ar"}'
```

### Supported tutoring/voice languages
- English (`en`)
- Spanish (`es`)
- French (`fr`)
- Portuguese (`pt`)
- Chinese Simplified (`zh-CN`)
- Chinese Traditional (`zh-TW`)
- Vietnamese (`vi`)
- Japanese (`ja`)
- Korean (`ko`)
- Italian (`it`)
- Arabic (`ar`)

See the `docs/` and `backend/` folders for implementation details.

## Gen Z UI Pack

Added an original **Canva-inspired** (not copied) visual system in:
- `docs/design-system.md`
- `frontend/src/app/globals.css`
- `frontend/src/components/GenZHomeMock.tsx`
- `frontend/src/app/page.tsx`

This gives your app a bold gradient, playful cards, streak-first layout, and mobile-friendly interaction style.
