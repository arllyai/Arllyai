# LinguaQuest AI

Production-ready blueprint for an AI-powered language learning platform inspired by Duolingo, with:

- Gamified progression (XP, streaks, hearts, badges, leaderboards)
- Adaptive lessons (vocabulary, grammar, listening, speaking)
- AI tutor powered by LLMs for personalized explanations and conversation
- Real-time voice support using ElevenLabs TTS (+ optional STT scoring)

## Stack

- **Frontend**: Next.js + Tailwind CSS (mobile-first)
- **Backend**: FastAPI (Python)
- **DB**: PostgreSQL
- **AI**: OpenAI API (exercise generation, tutor, personalization)
- **Voice**: ElevenLabs API
- **Infra**: Redis cache, S3-compatible blob storage, background workers

See the `docs/` and `backend/` folders for implementation details.
