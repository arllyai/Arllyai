# 5) Example Lesson Flow

1. User taps **Start Lesson**.
2. Backend selects next lesson via adaptive policy:
   - Inputs: recent accuracy, mistake tags, response latency, streak risk.
   - Output: lesson + targeted exercises.
3. For each exercise:
   - Render prompt and optional audio.
   - For speaking: play target phrase (ElevenLabs), record learner audio, score pronunciation.
   - Return correctness + concise AI feedback.
4. Mid-lesson adaptation:
   - If error rate > threshold, downgrade difficulty and inject scaffold hints.
   - If confidence high, add challenge item.
5. End of lesson:
   - XP, hearts change, streak update.
   - Save mistake taxonomy (e.g., article misuse, verb tense).
   - Show AI-generated recap and next recommendation.
