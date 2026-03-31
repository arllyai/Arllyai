# 1) App Architecture Diagram

```mermaid
flowchart LR
    U[Web/Mobile Client\nNext.js/React Native] -->|HTTPS| API[FastAPI API Gateway]
    API --> AUTH[Auth Service\nEmail + OAuth + JWT]
    API --> LEARN[Learning Engine\nAdaptive Lesson Orchestrator]
    API --> GAME[Gamification Service\nXP, Streaks, Hearts, Badges]
    API --> PROG[Progress Analytics Service]
    API --> TUTOR[AI Tutor Service\nOpenAI]
    API --> VOICE[Voice Service\nElevenLabs TTS/STT adapter]

    LEARN --> DB[(PostgreSQL)]
    GAME --> DB
    PROG --> DB
    AUTH --> DB
    TUTOR --> DB

    VOICE --> REDIS[(Redis Audio Cache)]
    VOICE --> BLOB[(S3/Blob Audio Store)]
    VOICE --> EL[ElevenLabs API]

    TUTOR --> OAI[OpenAI API]

    API --> QUEUE[Background Jobs\nCelery/RQ]
    QUEUE --> VOICE
    QUEUE --> PROG
```

## Scalability Notes
- Stateless API pods behind load balancer.
- Read replicas for analytics and leaderboard reads.
- Redis for hot cache (audio, sessions, leaderboard snapshots).
- Async jobs for TTS pre-generation, recommendation updates, and badge calculations.
- Event-driven telemetry (`lesson_completed`, `mistake_made`, `streak_updated`) for personalization.
