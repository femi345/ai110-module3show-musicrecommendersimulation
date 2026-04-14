# Reflection: Music Recommender Simulation

## Profile comparisons

### Happy Pop Fan vs. Chill Lofi Listener

These two are basically opposite vibes. The pop fan's list is all upbeat, high energy stuff (Sunrise City at 0.82 energy), and the lofi listener gets mellow, slow tracks (Library Rain at 0.35 energy). Makes sense.

One thing I noticed: Focus Flow (lofi/focused) shows up in the lofi listener's top 3 even though its mood is "focused," not "chill." The genre bonus alone (+2.0) is enough to carry it past songs that actually match the mood but are in the wrong genre. That's a pretty clear sign that genre is weighted too heavily.

### Intense Rock Lover vs. EDM Party Goer

Both want high energy, but they split on genre and valence. The rock fan gets Storm Runner and Rage Circuit (aggressive, lower valence). The EDM fan gets Afterparty Haze and Neon Basement (danceable, higher valence).

Gym Hero shows up in both lists. It has extreme energy (0.93) and its mood is tagged "intense," so it scores well for the rock profile, and its high danceability (0.88) helps it sneak into the EDM list too. Kind of interesting that one song can fit two very different listeners just by being high-energy.

### Sad & Acoustic vs. Happy Pop Fan

The most extreme contrast. Sad/acoustic user gets Ghost Town Blues at #1 (the only blues track), then a bunch of lofi songs that happen to have low energy. The happy pop fan gets none of those songs. Zero overlap in their top 5s.

This is where the filter bubble is most obvious. The system would never show the sad-music listener something upbeat that they might actually be in the mood for sometimes. It just keeps feeding them more of the same.

## Experiment observations

I halved genre weight (2.0 to 1.0) and doubled energy weight for the Happy Pop Fan profile. Rooftop Lights (indie pop, not pop) climbed to #2 because its energy (0.76) is close to the 0.80 target. Under default weights it was #3 behind Gym Hero. The weight shift hurt Gym Hero because its genre bonus shrank and its energy gap (0.93 vs 0.80) got punished harder.

So yeah, the default system is basically a genre matcher with energy as a tiebreaker. Changing that balance made the results feel more about the actual vibe of the music and less about the label.

## What I learned

Recommendation is just sorting. Score everything, sort descending, take the top. That's it. The "intelligence" is entirely in how you calculate that score. And what I didn't expect is how much the output changes from one small weight tweak. I keep coming back to that, because it means whoever picks the weights is basically deciding what people listen to, and they might not even think of it that way.
