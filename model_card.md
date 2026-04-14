# Model Card: Music Recommender Simulation

## 1. Model name

VibeFinder 1.0

---

## 2. Intended use

Suggests 5 songs from a 20-song catalog based on a user's preferred genre, mood, and energy. This is a classroom project for exploring how content-based filtering works. Not meant for real listeners.

---

## 3. How it works

The system loops through every song and gives it a score based on how well it matches the user's taste profile. Genre match is worth the most (+2 points). Mood match gets +1. Then there are smaller bonuses for how close the song's energy, valence, and danceability are to what the user wants.

So if you say you like pop, happy, energy 0.8, a pop/happy song with energy 0.82 is going to score close to 5. A jazz/relaxed song with energy 0.37 is going to score around 1.5.

After every song has a score, they get sorted highest to lowest and the top 5 come back with a list of reasons (like "genre match (+2.0), energy similarity (+0.98)").

---

## 4. Data

The catalog has 20 songs in `data/songs.csv`. Started with 10 from the template, added 10 more to cover genres that were missing (blues, metal, folk, hip-hop, etc.).

Genres: pop, lofi, rock, ambient, jazz, synthwave, indie pop, country, edm, r&b, hip-hop, classical, blues, electronic, folk, metal.

Moods: happy, chill, intense, relaxed, moody, focused, romantic, sad.

It's all hand-picked and skews toward English-language Western music. Some genres only have a single song, which means the system can't really give variety for those.

---

## 5. Strengths

When someone has straightforward taste ("I like pop and happy music"), the top result is basically always the obvious pick. It got Sunrise City for the pop fan, Library Rain for the lofi listener, Storm Runner for the rock fan. Hard to argue with those.

The reasons list is probably the best part. You can see exactly why each song was picked and which features mattered. Nothing is hidden.

It's also easy to tinker with. Change a weight, rerun, see what happens. Good for learning.

---

## 6. Limitations and bias

Genre gets 2 points out of a max of 5. That's 40% of the score from one exact string comparison. So the system will almost always rank same-genre songs first, even if a different song matches the user's vibe better on every other dimension. That's a filter bubble.

With only 20 songs, some genres have one entry. The blues fan gets Ghost Town Blues at #1 every time with no alternative. Metal fans get Rage Circuit and that's it.

The mood matching is rigid. "chill" and "relaxed" are different strings, so they get zero overlap. A real person would consider those almost interchangeable.

There's no collaborative signal at all. It can't say "people who liked this also liked that." It only knows what one user typed in.

And obviously: no lyrics, no language, no release date, no listening history. Real recommenders use all of those.

---

## 7. Evaluation

I tested five profiles:

| Profile | Top result | Makes sense? |
|---------|-----------|------------|
| Happy Pop Fan | Sunrise City (pop/happy) | Yeah |
| Chill Lofi Listener | Library Rain (lofi/chill) | Yeah |
| Intense Rock Lover | Storm Runner (rock/intense) | Yeah |
| Sad & Acoustic | Ghost Town Blues (blues/sad) | Yeah |
| EDM Party Goer | Afterparty Haze (edm/happy) | Yeah |

I also ran an experiment where I halved the genre weight (2.0 to 1.0) and doubled energy (1.0 to 2.0). Rooftop Lights (indie pop) jumped to #2 for the pop fan profile because its energy is close to the target. That confirmed what I suspected: genre was eating everything else.

---

## 8. Future work

- Fuzzy mood matching, so "chill" and "relaxed" aren't treated as completely different.
- A diversity penalty that stops the same genre from dominating all 5 slots.
- Some form of collaborative filtering, even if it's just hardcoded ("users who like lofi also tend to like ambient").

---

## 9. Personal reflection

Honestly, I was surprised how "real" the results felt from such a simple system. Three rules and some addition, and it already looks like a recommendations page. That was cool but also kind of made me uneasy, because if this toy version can create a believable filter bubble, imagine what happens at Spotify's scale with hundreds of signals.

Copilot was useful for brainstorming the initial scoring approach and generating the extra CSV rows. But the weights themselves, I had to adjust by hand after seeing the output. The first version I tried had genre at 3.0 and everything else was irrelevant. It took a few rounds of running the profiles and eyeballing results before the weights felt balanced.

The weight shift experiment was what really got me. One number change and the entire top 5 reshuffled. If that's happening in a real app, whoever decides how much genre matters vs. energy vs. mood is basically choosing what music people hear. I don't think most engineers think about it that way, but they probably should.
