-- 2) Database Schema (PostgreSQL)

CREATE TABLE users (
  id UUID PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT,
  oauth_provider TEXT,
  oauth_subject TEXT,
  display_name TEXT NOT NULL,
  target_language TEXT NOT NULL,
  native_language TEXT NOT NULL,
  daily_goal_minutes INT DEFAULT 10,
  privacy_mode BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE user_stats (
  user_id UUID PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
  xp INT DEFAULT 0,
  level INT DEFAULT 1,
  streak_days INT DEFAULT 0,
  longest_streak INT DEFAULT 0,
  hearts INT DEFAULT 5,
  accuracy NUMERIC(5,2) DEFAULT 0,
  last_active_date DATE,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE courses (
  id UUID PRIMARY KEY,
  language_code TEXT NOT NULL,
  title TEXT NOT NULL,
  difficulty TEXT CHECK (difficulty IN ('beginner','intermediate','advanced')),
  is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE lessons (
  id UUID PRIMARY KEY,
  course_id UUID REFERENCES courses(id) ON DELETE CASCADE,
  unit_index INT NOT NULL,
  lesson_index INT NOT NULL,
  lesson_type TEXT CHECK (lesson_type IN ('vocabulary','grammar','listening','speaking','mixed')),
  title TEXT NOT NULL,
  objectives JSONB NOT NULL,
  base_difficulty INT DEFAULT 1
);

CREATE TABLE exercises (
  id UUID PRIMARY KEY,
  lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
  exercise_type TEXT CHECK (exercise_type IN ('mcq','fill_blank','ordering','listening','speaking')),
  prompt TEXT NOT NULL,
  choices JSONB,
  correct_answer JSONB NOT NULL,
  explanation TEXT,
  difficulty INT DEFAULT 1,
  audio_text TEXT,
  audio_cache_key TEXT
);

CREATE TABLE lesson_attempts (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
  score NUMERIC(5,2) NOT NULL,
  accuracy NUMERIC(5,2) NOT NULL,
  xp_earned INT NOT NULL,
  hearts_lost INT DEFAULT 0,
  started_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  metadata JSONB
);

CREATE TABLE exercise_attempts (
  id UUID PRIMARY KEY,
  lesson_attempt_id UUID REFERENCES lesson_attempts(id) ON DELETE CASCADE,
  exercise_id UUID REFERENCES exercises(id) ON DELETE CASCADE,
  user_answer JSONB,
  is_correct BOOLEAN,
  latency_ms INT,
  pronunciation_score NUMERIC(5,2),
  feedback TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE achievements (
  id UUID PRIMARY KEY,
  code TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  xp_reward INT DEFAULT 0
);

CREATE TABLE user_achievements (
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  achievement_id UUID REFERENCES achievements(id) ON DELETE CASCADE,
  earned_at TIMESTAMPTZ DEFAULT NOW(),
  PRIMARY KEY (user_id, achievement_id)
);

CREATE TABLE leaderboard_daily (
  leaderboard_date DATE NOT NULL,
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  xp_gained INT NOT NULL,
  rank INT,
  PRIMARY KEY (leaderboard_date, user_id)
);

CREATE TABLE voice_assets (
  id UUID PRIMARY KEY,
  cache_key TEXT UNIQUE NOT NULL,
  text_hash TEXT NOT NULL,
  voice_id TEXT NOT NULL,
  model_id TEXT NOT NULL,
  audio_url TEXT NOT NULL,
  duration_ms INT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_lessons_course ON lessons(course_id);
CREATE INDEX idx_exercises_lesson ON exercises(lesson_id);
CREATE INDEX idx_attempts_user_completed ON lesson_attempts(user_id, completed_at DESC);
CREATE INDEX idx_leaderboard_date_rank ON leaderboard_daily(leaderboard_date, rank);
