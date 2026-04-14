# Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

This recommender suggests 5 songs from a 20-song catalog based on a user's preferred genre, mood, and energy level. It is built for classroom exploration of how content-based filtering works. It is not intended for production use with real listeners.

---

## 3. How the Model Works

The system compares every song in the catalog against a user's taste profile. Each song gets points for:

- **Genre match** (worth the most, +2 points) -- if the song's genre is exactly what the user likes.
- **Mood match** (+1 point) -- if the song's mood tag matches the user's preferred mood.
- **Energy similarity** (up to +1 point) -- songs whose energy level is closest to the user's target score higher. A song with energy 0.82 and a user target of 0.80 scores almost a full point, while a song at 0.20 scores much less.
- **Valence and danceability similarity** (up to +0.5 each) -- same "closeness" idea, at half weight.

After every song has a total score, the system sorts them highest-to-lowest and returns the top 5.

---

## 4. Data

- The catalog contains **20 songs** in `data/songs.csv`.
- The original starter had 10 songs; 10 more were added to increase genre diversity.
- Genres represented: pop, lofi, rock, ambient, jazz, synthwave, indie pop, country, edm, r&b, hip-hop, classical, blues, electronic, folk, metal.
- Moods represented: happy, chill, intense, relaxed, moody, focused, romantic, sad.
- The dataset was hand-curated and is small. It does not reflect the actual distribution of music in the real world, and it skews toward English-language Western genres.

---

## 5. Strengths

- For users with clear-cut tastes (e.g., "I like pop and happy music"), the top result is almost always the most intuitive pick.
- The "reasons" list next to every recommendation makes it transparent why a song was chosen -- no black-box mystery.
- Simple enough to modify weights and immediately see the effect on rankings, which makes it a good teaching tool.

---

## 6. Limitations and Bias

- **Genre dominance:** With +2.0 for a genre match, the system almost always puts same-genre songs at the top, even if another song matches every other attribute perfectly. This creates a "filter bubble" where users never discover music outside their stated genre.
- **Small catalog:** 20 songs means some genres only have one entry (e.g., blues, metal). A user who likes blues will always see Ghost Town Blues at #1 with no variety.
- **No collaborative signal:** The system only knows what one user says they like. It cannot learn from patterns across users (e.g., "people who like X also like Y").
- **Exact string matching:** A user who says mood="chill" gets zero mood points for a song tagged "relaxed," even though those are similar vibes.
- **Missing context:** The system ignores lyrics, language, release date, artist familiarity, and listening history -- all things that real recommenders use.

---

## 7. Evaluation

Five user profiles were tested:

| Profile | Top Result | Intuitive? |
|---------|-----------|------------|
| Happy Pop Fan | Sunrise City (pop/happy) | Yes |
| Chill Lofi Listener | Library Rain (lofi/chill) | Yes |
| Intense Rock Lover | Storm Runner (rock/intense) | Yes |
| Sad & Acoustic | Ghost Town Blues (blues/sad) | Yes |
| EDM Party Goer | Afterparty Haze (edm/happy) | Yes |

**Experiment -- Weight Shift:**
When genre weight was halved (2.0 to 1.0) and energy weight doubled (1.0 to 2.0), Rooftop Lights (indie pop) jumped into the #2 slot for the Happy Pop Fan profile because its energy closely matched the target. This confirmed that the default weights over-index on genre.

---

## 8. Future Work

- **Fuzzy mood matching:** Treat "chill" and "relaxed" as similar rather than distinct.
- **Diversity penalty:** Penalize repeated artists or genres in the top results so recommendations feel more varied.
- **Collaborative filtering:** Let multiple user profiles influence each other (e.g., "users similar to you also liked...").

---

## 9. Personal Reflection

Building this system made concrete how even a tiny set of rules -- genre match, mood match, energy gap -- is enough to produce results that *feel* personalized. That is both impressive and a little unsettling, because it also shows how easy it is for a simple system to lock someone into a filter bubble just by giving full weight to one feature like genre.

Using AI tools throughout the process was helpful for brainstorming scoring strategies and generating diverse CSV data, but the weights and the evaluation still required human judgment. Copilot suggested a scoring formula, but I had to tune the weights after seeing that genre was dominating every list.

The biggest surprise was how much the ranking changes from one small weight tweak. Halving the genre bonus and doubling energy completely reshuffled the top 5. In a real app with millions of users, that kind of sensitivity means product decisions about weights directly shape what culture people consume -- which is a responsibility worth thinking about.
