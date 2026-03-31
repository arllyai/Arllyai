# Canva-Inspired (Not Copied) Gen Z Design System

> We cannot directly copy Canva proprietary designs. This system is an original style direction inspired by modern playful creator tools.

## Visual Direction
- **Tone**: energetic, friendly, creator-first.
- **Shape language**: rounded-2xl cards, soft shadows, chunky CTA buttons.
- **Motion**: quick spring transitions (120–220ms), confetti on milestones.
- **Layout**: mobile-first, sticky XP/streak header, bottom tab navigation.

## Color Tokens
- `brand.violet`: `#7C3AED`
- `brand.pink`: `#EC4899`
- `brand.sky`: `#38BDF8`
- `brand.lime`: `#84CC16`
- `surface.0`: `#0B1020`
- `surface.1`: `#121A33`
- `text.primary`: `#F9FAFB`
- `text.muted`: `#A5B4FC`

Use a gradient primary: `linear-gradient(135deg, #7C3AED 0%, #EC4899 55%, #38BDF8 100%)`.

## Typography
- Headings: **Plus Jakarta Sans** (700/800)
- Body: **Inter** (400/500)
- Numbers/XP: **Space Grotesk**

## Components
1. **Lesson Node**
   - Circular token with progress ring and emoji badge.
2. **XP Chip**
   - Gradient pill with glow (`shadow-[0_0_30px_rgba(124,58,237,.45)]`).
3. **Hearts Meter**
   - Heart icons + animated shake on mistake.
4. **Tutor Bubble**
   - Rounded 24px speech card; correction chips in contrasting pastel.
5. **Pronunciation Card**
   - Waveform strip + “Listen” and “Record” dual CTA.

## Micro-interactions
- Correct answer: pop + green glow (scale 1 -> 1.06 -> 1).
- Wrong answer: horizontal shake + hearts decrement animation.
- Streak milestone: flame pulse + confetti burst.

## Accessibility
- Keep text contrast >= WCAG AA.
- Minimum tap target 44x44px.
- Disable motion if `prefers-reduced-motion`.
