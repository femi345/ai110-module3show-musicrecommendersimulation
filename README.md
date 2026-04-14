# Music Recommender Simulation

## Project Summary

A content-based music recommendation system built in Python. Given a user's taste profile (genre, mood, energy, valence, danceability), it scores every song in a 20-track catalog using weighted attribute matching and returns the top 5 results with human-readable explanations for each pick.

---

## How The System Works

### Real-World Context

Streaming platforms like Spotify use two main strategies: **collaborative filtering** (finding users with similar listening history and recommending what they liked) and **content-based filtering** (matching song attributes like tempo, energy, and genre to a user's stated preferences). This project implements a simplified version of content-based filtering.

### Features Used

Each **Song** has: `genre`, `mood`, `energy` (0-1), `tempo_bpm`, `valence` (0-1), `danceability` (0-1), `acousticness` (0-1).

Each **UserProfile** stores: `favorite_genre`, `favorite_mood`, `target_energy`, and optionally `valence` and `danceability` targets.

### Algorithm Recipe

For each song, the scoring function computes:

| Rule | Points | Logic |
|------|--------|-------|
| Genre match | +2.0 | Exact string match between user's genre and song's genre |
| Mood match | +1.0 | Exact string match between user's mood and song's mood |
| Energy similarity | 0 to +1.0 | `1.0 - abs(song_energy - target_energy)` |
| Valence similarity | 0 to +0.5 | `(1.0 - abs(song_valence - target_valence)) * 0.5` |
| Danceability similarity | 0 to +0.5 | `(1.0 - abs(song_dance - target_dance)) * 0.5` |

Maximum possible score: **5.0**. Songs are sorted by score descending, and the top *k* are returned.

### Potential Bias

This system is likely to over-prioritize genre because it carries the highest weight. A song that matches genre but misses on mood and energy can still outscore a song that matches mood, energy, valence, and danceability but is in the wrong genre. This creates a filter bubble for genre-loyal users.

---

## Getting Started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
python -m src.main
```

### Tests

```bash
pytest
```

---

## Experiments

### Weight Shift: Genre halved, Energy doubled

Changed genre bonus from 2.0 to 1.0 and energy weight from 1x to 2x for the "Happy Pop Fan" profile.

**Result:** Rooftop Lights (indie pop) climbed from #3 to #2 because its energy (0.76) is very close to the target (0.80). Gym Hero dropped from #2 to #4 because its energy gap (0.93 vs 0.80) became more costly under doubled energy weight.

**Conclusion:** The default weights over-index on genre. When energy is weighted more heavily, the system becomes more sensitive to "vibe" and less locked into genre labels.

---

## Limitations and Risks

- Only works on a 20-song catalog -- too small for real use.
- Exact string matching on genre and mood means "chill" and "relaxed" are treated as completely different.
- No understanding of lyrics, language, or cultural context.
- Genre carries the highest weight, creating a filter bubble that reinforces existing preferences.
- No collaborative signal -- it cannot learn from other users' behavior.

---

## Reflection

See the full [Model Card](model_card.md) and [Reflection](reflection.md).

Building this recommender showed how a small set of rules -- match genre, match mood, compare energy -- is enough to produce results that feel personalized. But it also revealed how easily a simple system creates filter bubbles. When genre carries double the weight of everything else, users will never see songs outside their comfort zone.

The weight-shift experiment was the most revealing moment: one small change to the scoring formula completely reshuffled the top 5 results. In a real product, that kind of sensitivity means the engineers choosing weights are directly shaping what music millions of people hear. That is a design responsibility as much as a technical one.
