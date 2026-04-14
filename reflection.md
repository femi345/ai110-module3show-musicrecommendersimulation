# Reflection: Music Recommender Simulation

## Profile Comparisons

**Happy Pop Fan vs. Chill Lofi Listener:**
The pop fan's top picks are high-energy, upbeat tracks (Sunrise City at 0.82 energy), while the lofi listener gets mellow, low-tempo songs (Library Rain at 0.35 energy). This makes sense because energy and genre pull in opposite directions for these two profiles. What is interesting is that Focus Flow (lofi/focused) still appears for the lofi listener even though its mood does not match "chill" -- the genre bonus alone carries it into the top 3.

**Intense Rock Lover vs. EDM Party Goer:**
Both profiles want high energy, but they diverge on genre and valence. The rock lover gets Storm Runner and Rage Circuit (aggressive, lower valence), while the EDM fan gets Afterparty Haze and Neon Basement (danceable, higher valence). The overlap is Gym Hero, which shows up in both lists because it has extreme energy (0.93) and the word "intense" in its mood. This highlights how a single song can bridge two very different listener types when it scores high on a shared feature.

**Sad & Acoustic vs. Happy Pop Fan:**
These profiles are nearly opposites. The sad/acoustic user gets Ghost Town Blues at #1 -- the only blues song in the catalog -- and then a cluster of lofi tracks that happen to share low energy. The happy pop fan gets none of those. This is the clearest example of the filter bubble: each profile sees a completely non-overlapping top 5, which means the system would never expose a sad-music listener to an upbeat song they might actually enjoy.

## Experiment Observations

When genre weight was halved (2.0 to 1.0) and energy weight was doubled, the Happy Pop Fan's results shifted noticeably. Rooftop Lights (indie pop, not pop) climbed to #2 because its energy (0.76) is close to the target. Under default weights it was #3 behind Gym Hero; the weight shift demoted Gym Hero because its genre bonus shrank and its energy gap (0.93 vs 0.80) became more costly. This confirmed that the default system over-rewards exact genre strings.

## What I Learned

The most useful takeaway is that recommendation is really just sorting -- score everything, sort descending, take the top. The "magic" is entirely in how you compute the score, and tiny changes to those numbers produce visibly different user experiences. That makes weight tuning one of the most impactful decisions in a recommender, and it is easy to get wrong or introduce bias without realizing it.
