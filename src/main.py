"""Command-line runner for the Music Recommender Simulation."""

from src.recommender import load_songs, recommend_songs


# ---------------------------------------------------------------------------
# User profiles
# ---------------------------------------------------------------------------

PROFILES = {
    "Happy Pop Fan": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "valence": 0.80,
        "danceability": 0.80,
    },
    "Chill Lofi Listener": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "valence": 0.58,
        "danceability": 0.55,
    },
    "Intense Rock Lover": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
        "valence": 0.45,
        "danceability": 0.65,
    },
    "Sad & Acoustic": {
        "genre": "blues",
        "mood": "sad",
        "energy": 0.40,
        "valence": 0.35,
        "danceability": 0.45,
    },
    "EDM Party Goer": {
        "genre": "edm",
        "mood": "happy",
        "energy": 0.90,
        "valence": 0.75,
        "danceability": 0.90,
    },
}


def display_recommendations(profile_name: str, prefs: dict, recs: list) -> None:
    """Print a formatted recommendation block for one user profile."""
    print("=" * 60)
    print(f"  Profile: {profile_name}")
    print(f"  Prefs  : genre={prefs['genre']}, mood={prefs['mood']}, "
          f"energy={prefs['energy']}")
    print("=" * 60)
    for rank, (song, score, explanation) in enumerate(recs, start=1):
        print(f"  #{rank}  {song['title']}  by {song['artist']}")
        print(f"       Score : {score:.2f}")
        print(f"       Why   : {explanation}")
        print()


def run_experiment(songs: list) -> None:
    """Run a weight-shift experiment: double energy weight, halve genre weight."""
    from src.recommender import score_song as original_score

    def experimental_score(user_prefs, song):
        score = 0.0
        reasons = []

        # Genre match — halved from 2.0 to 1.0
        if song["genre"].lower() == user_prefs.get("genre", "").lower():
            score += 1.0
            reasons.append("genre match (+1.0, halved)")

        # Mood match — unchanged
        if song["mood"].lower() == user_prefs.get("mood", "").lower():
            score += 1.0
            reasons.append("mood match (+1.0)")

        # Energy similarity — doubled from 1.0 to 2.0
        target_energy = user_prefs.get("energy", 0.5)
        energy_sim = 1.0 - abs(song["energy"] - target_energy)
        bonus = energy_sim * 2.0
        score += bonus
        reasons.append(f"energy similarity x2 (+{bonus:.2f})")

        return (score, reasons)

    print("\n" + "#" * 60)
    print("  EXPERIMENT: Genre weight halved, Energy weight doubled")
    print("#" * 60)

    test_profile = PROFILES["Happy Pop Fan"]
    scored = []
    for song in songs:
        total, reasons = experimental_score(test_profile, song)
        scored.append((song, total, "; ".join(reasons)))
    scored.sort(key=lambda x: x[1], reverse=True)

    display_recommendations("Happy Pop Fan (EXPERIMENT)", test_profile, scored[:5])


def main() -> None:
    songs = load_songs("data/songs.csv")

    for name, prefs in PROFILES.items():
        recs = recommend_songs(prefs, songs, k=5)
        display_recommendations(name, prefs, recs)

    run_experiment(songs)


if __name__ == "__main__":
    main()
