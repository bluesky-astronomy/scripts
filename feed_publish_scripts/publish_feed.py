from atproto import Client, models
from pathlib import Path
import os
import time


# MAIN ENVIRONMENT VARIABLES
HANDLE: str = "emily.space"
PASSWORD: str = os.getenv("BLUESKY_PASSWORD")
HOSTNAME: str = "feed-all.astronomy.blue"
AVATAR_LOCATIONS: Path = Path("/home/emily/bluesky/branding/jpg")
SERVICE_DID: str = ""  # Only use this if you want a service did different from did:web

# FEED NAMES AND DESCRIPTIONS
FEEDS = {
    "astro-all": {
        "DISPLAY_NAME": "Astrosky",
        "DESCRIPTION": "All posts from the astronomy community on Bluesky. Signup to post here via @bot.astronomy.blue",
        "AVATAR_PATH": AVATAR_LOCATIONS / "astro-all.jpg",
    },
    "astro": {
        "DISPLAY_NAME": "Astronomy",
        "DESCRIPTION": "Astronomy posts, from astronomers!\nAny astronomer can post here by signing up via @bot.astronomy.blue\nContains posts from signed up users with a 🔭, #astronomy, or #astro.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "astro.jpg",
    },
    "astrophotos": {
        "DISPLAY_NAME": "Astrophotography",
        "DESCRIPTION": "Astrophotography posts, from astrophotographers! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #astrophotography or #astrophotos.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "astrophotos.jpg",
    },
    # ASTRONOMY TOPICS
    "cosmology": {
        "DISPLAY_NAME": "Cosmology",
        "DESCRIPTION": "A science-oriented feed about cosmology! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #cosmology.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "cosmology.jpg",
    },
    "exoplanets": {
        "DISPLAY_NAME": "Exoplanets",
        "DESCRIPTION": "A science-oriented feed about exoplanets! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #exoplanet or #exoplanets.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "exoplanets.jpg",
    },
    "extragalactic": {
        "DISPLAY_NAME": "Extragalactic Astronomy",
        "DESCRIPTION": "A science-oriented feed about extragalactic astronomy! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #extragalactic.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "extragalactic.jpg",
    },
    "highenergy": {
        "DISPLAY_NAME": "High Energy Astrophysics",
        "DESCRIPTION": "A science-oriented feed about high-energy astronomy and astroparticle physics! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #highenergyastro.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "highenergy.jpg",
    },
    "instrumentation": {
        "DISPLAY_NAME": "Astro Instrumentation",
        "DESCRIPTION": "A science-oriented feed about astronomical instrumentation! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #instrumentation.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "instrumentation.jpg",
    },
    "methods": {
        "DISPLAY_NAME": "Methods for Astronomy",
        "DESCRIPTION": "A feed to discuss methods and software for astronomy research! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #astromethods, #astrocoding, or #astrocode.", #\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "methods.jpg",
    },
    "milkyway": {
        "DISPLAY_NAME": "The Milky Way",
        "DESCRIPTION": "A science-oriented feed about our galaxy (and everything that orbits it). Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #milkyway.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "milkyway.jpg",
    },
    "planetary": {
        "DISPLAY_NAME": "Planetary Science",
        "DESCRIPTION": "A science-oriented feed about planetary science! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #planetaryscience or #planetsci.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "planetary.jpg",
    },
    "radio": {
        "DISPLAY_NAME": "Radio Astronomy",
        "DESCRIPTION": "A science-oriented feed about radio astronomy! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #radioastronomy or #radioastro.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "radio.jpg",
    },
    # "solar": {
    #     "DISPLAY_NAME": "",
    #     "DESCRIPTION": "",
    #     "AVATAR_PATH": AVATAR_LOCATIONS / "",
    # },
    "stellar": {
        "DISPLAY_NAME": "Stellar Astronomy",
        "DESCRIPTION": "A science-oriented feed about stars! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #stars, #stellarastrononomy or #stellarastro.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "stellar.jpg",
    },
    # ASTRONOMY / OTHER
    "education": {
        "DISPLAY_NAME": "Astronomy Education",
        "DESCRIPTION": "A feed about astronomy education! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #astroeducation or #astroedu.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "history.jpg",
    },
    "history": {
        "DISPLAY_NAME": "History of Astronomy",
        "DESCRIPTION": "A feed about the history of astronomy and astrophysics! Part of the Astronomy feeds network.\nAstronomers can sign up to post here via @bot.astronomy.blue\nContains posts from signed up users with #astrohistory or #historyofastronomy.\nPosts here are also included in the main Astronomy feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "history.jpg",
    },
    # "questions": {
    #     "DISPLAY_NAME": "",
    #     "DESCRIPTION": "",
    #     "AVATAR_PATH": AVATAR_LOCATIONS / "",
    # },

    # MAINTENANCE PURPOSES
    "signup": {
        "DISPLAY_NAME": "Astrofeed Signups",
        "DESCRIPTION": "A feed for Astronomy feed moderators that shows users waiting to sign up to the feed.",
        "AVATAR_PATH": AVATAR_LOCATIONS / "questions.jpg",
    },
}

# If SERVICE_DID is defined
FEED_DID = SERVICE_DID
if not FEED_DID:
    FEED_DID = f"did:web:{HOSTNAME}"


def upload_feed(record_name, client=None):
    """Function that uploads a feed."""
    print(f"Publishing feed {record_name}")

    if client is None:
        client = get_client()

    display_name, description, avatar_path = (
        FEEDS[record_name]["DISPLAY_NAME"],
        FEEDS[record_name]["DESCRIPTION"],
        FEEDS[record_name]["AVATAR_PATH"],
    )

    avatar_blob = None
    if avatar_path:
        with open(avatar_path, "rb") as f:
            avatar_data = f.read()
            avatar_blob = client.com.atproto.repo.upload_blob(avatar_data).blob

    response = client.com.atproto.repo.put_record(
        models.ComAtprotoRepoPutRecord.Data(
            repo=client.me.did,
            collection=models.ids.AppBskyFeedGenerator,
            rkey=record_name,
            record=models.AppBskyFeedGenerator.Record(
                did=FEED_DID,
                display_name=display_name,
                description=description,
                avatar=avatar_blob,
                created_at=client.get_current_time_iso(),
            ),
        )
    )

    print(f"-> Successfully published feed {record_name}")
    print(f"-> Feed URI: {response.uri}")


def get_client():
    client = Client()
    client.login(HANDLE, PASSWORD)
    return client


if __name__ == "__main__":
    client = get_client()
    # Upload all:
    for feed in FEEDS:
        upload_feed(feed, client=client)
        time.sleep(1)  # Just to be less spammy

    # Upload just one:
    # upload_feed('signup', client=client)
