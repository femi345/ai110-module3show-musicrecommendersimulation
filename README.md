# Music Recommender Simulation

## Project summary

I built a simple music recommender in Python. You give it a taste profile (genre, mood, energy, etc.) and it scores every song in a 20-track catalog, then spits out the top 5 with reasons for each pick.

---

## How the system works

### Real world context

Spotify-style platforms generally use two approaches: collaborative filtering, where they look at what similar users listened to, and content-based filtering, where they match song attributes (tempo, energy, genre) against what you say you like. This project does the second one, in a very stripped-down way.

### Features used

Each song has: `genre`, `mood`, `energy` (0-1), `tempo_bpm`, `valence` (0-1), `danceability` (0-1), `acousticness` (0-1).

A user profile stores: `favorite_genre`, `favorite_mood`, `target_energy`, and optionally `valence` and `danceability` targets.

### Algorithm recipe

For each song, the scoring function adds up points:

| Rule | Points | Logic |
|------|--------|-------|
| Genre match | +2.0 | Exact string match between user's genre and song's genre |
| Mood match | +1.0 | Exact string match between user's mood and song's mood |
| Energy similarity | 0 to +1.0 | `1.0 - abs(song_energy - target_energy)` |
| Valence similarity | 0 to +0.5 | `(1.0 - abs(song_valence - target_valence)) * 0.5` |
| Danceability similarity | 0 to +0.5 | `(1.0 - abs(song_dance - target_dance)) * 0.5` |

Max score is 5.0. Songs get sorted highest to lowest, top *k* get returned.

### Potential bias

Genre carries the most weight by far. A song can match on mood, energy, valence, and danceability but still lose to a song that only matches on genre. That means the system basically locks you into whatever genre you said you liked.

---

## Getting started

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

### Weight shift: genre halved, energy doubled

I changed genre bonus from 2.0 to 1.0 and doubled the energy weight for the "Happy Pop Fan" profile.

Rooftop Lights (indie pop) jumped from #3 to #2 because its energy (0.76) is almost exactly the target (0.80). Gym Hero dropped from #2 to #4 because its energy gap (0.93 vs 0.80) got punished harder under the new weights.

Takeaway: the default scoring over-indexes on genre. Bumping up energy made the results feel more "vibe-aware" and less about matching a label.

---

## Limitations

- 20 songs is tiny. Some genres only have one track, so there's zero variety for those users.
- "chill" and "relaxed" are treated as totally different moods because it's exact string matching. No fuzzy logic.
- Doesn't know anything about lyrics, language, or listening history.
- Genre being worth 2x everything else creates a pretty obvious filter bubble.
- Can't learn from other users. It only knows what one person told it.

---

## Reflection

See the full [Model Card](model_card.md) and [Reflection](reflection.md).

The thing that stuck with me is how little it takes for a system like this to feel like it "knows" you. Three rules and some weights, and the results actually look reasonable. But that's also what makes it dangerous in a real product, because the person choosing those weights is deciding what people hear, and most users would never know.

The weight shift experiment drove that home. I changed one number and the top 5 reshuffled completely. If Spotify did that, millions of people would hear different music tomorrow.
