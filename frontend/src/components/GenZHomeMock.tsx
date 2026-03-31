import { Logo } from "./Logo";

export function GenZHomeMock() {
  return (
    <main style={{ maxWidth: 420, margin: "0 auto", padding: "1rem" }}>
      <header className="card" style={{ marginBottom: "1rem" }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <Logo size="md" />
          <Logo size="xs" markOnly />
        </div>
      </header>

      <header className="card" style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <div style={{ fontSize: 12, color: "var(--text-muted)" }}>Daily Streak</div>
          <div style={{ fontWeight: 800, fontSize: 24 }}>🔥 12 days</div>
        </div>
        <div className="xp-chip">+245 XP</div>
      </header>

      <section className="card" style={{ marginTop: "1rem" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <h2 style={{ marginTop: 0 }}>Continue Lesson</h2>
          <Logo size="sm" markOnly />
        </div>
        <p style={{ color: "var(--text-muted)" }}>Spanish • Unit 4 • Speaking drill</p>
        <button className="gradient-cta">Start 5-min Sprint</button>
      </section>

      <section className="card" style={{ marginTop: "1rem" }}>
        <h3 style={{ marginTop: 0 }}>AI Tutor Tip</h3>
        <p style={{ marginBottom: 0 }}>
          Great work! Practice past tense endings with 3 short speaking prompts today.
        </p>
      </section>
    </main>
  );
}
