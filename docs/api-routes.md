# 3) API Routes

## Auth
- `POST /v1/auth/signup`
- `POST /v1/auth/login`
- `GET /v1/auth/oauth/{provider}/start`
- `GET /v1/auth/oauth/{provider}/callback`
- `POST /v1/auth/refresh`

## Profile & Goals
- `GET /v1/me`
- `PATCH /v1/me`
- `PATCH /v1/me/goals`
- `GET /v1/me/privacy`
- `PATCH /v1/me/privacy`

## Courses & Lessons
- `GET /v1/courses`
- `GET /v1/courses/{course_id}/path`
- `GET /v1/lessons/{lesson_id}`
- `POST /v1/lessons/{lesson_id}/start`
- `POST /v1/lessons/{lesson_id}/submit`

## Exercises
- `POST /v1/exercises/generate` (AI dynamic generation)
- `POST /v1/exercises/{exercise_id}/check`

## AI Tutor
- `POST /v1/tutor/chat`
- `POST /v1/tutor/explain`
- `POST /v1/tutor/conversation-sim`

## Voice (ElevenLabs)
- `POST /v1/voice/tts` (text -> audio URL/stream)
- `GET /v1/voice/tts/{asset_id}`
- `POST /v1/voice/pronunciation/score` (optional STT + scoring)

## Gamification
- `GET /v1/gamification/stats`
- `GET /v1/gamification/leaderboard?range=daily|weekly`
- `GET /v1/gamification/achievements`
- `POST /v1/gamification/hearts/refill`

## Dashboard
- `GET /v1/dashboard/overview`
- `GET /v1/dashboard/weak-areas`
- `GET /v1/dashboard/recommendations`
