"""
Google Photos review collector — run this on YOUR OWN laptop (needs normal internet access).

What it does:
- Pulls real Play Store reviews for Google Photos
- Pulls real App Store reviews for Google Photos
- Filters to ones that actually mention searching / finding / remembering a photo
- Writes them into a plain text file, one review per line, ready to paste into the discovery engine tool

Setup (run once in a terminal):
    pip install google-play-scraper app-store-scraper

Then run:
    python collect_reviews.py
"""

from google_play_scraper import reviews, Sort
import re

try:
    from app_store_scraper import AppStore
    APP_STORE_AVAILABLE = True
except Exception as e:
    APP_STORE_AVAILABLE = False
    print(f"(App Store scraper not available/broken on this machine, skipping it: {e})")

# Keywords that suggest the review is actually about search / retrieval, not something unrelated
# (storage, pricing, sync bugs, etc). Feel free to add more words you notice while reading.
RELEVANT_KEYWORDS = [
    "search", "find", "found", "remember", "recall", "looking for",
    "can't locate", "cant locate", "old photo", "old photos", "ask photos",
    "gemini", "keyword", "scroll", "date", "location", "screenshot",
    "album", "memory", "memories"
]

def is_relevant(text: str) -> bool:
    t = text.lower()
    return any(kw in t for kw in RELEVANT_KEYWORDS)


def clean(text: str) -> str:
    # collapse newlines/extra spaces so each review becomes one clean line
    return re.sub(r"\s+", " ", text).strip()


def collect_play_store(app_id="com.google.android.apps.photos", target=250):
    print(f"Fetching Play Store reviews for {app_id} ...")
    collected = []
    continuation_token = None
    while len(collected) < target:
        result, continuation_token = reviews(
            app_id,
            lang="en",
            country="us",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token,
        )
        if not result:
            break
        for r in result:
            content = clean(r["content"])
            if content and is_relevant(content):
                score = r.get("score", "")
                date = str(r.get("at", ""))[:10]
                collected.append(f"Play Store review ({date}, {score}\u2605): {content}")
        print(f"  ...{len(collected)} relevant reviews so far")
        if continuation_token is None:
            break
    return collected[:target]


def collect_app_store(app_name="google-photos", app_id=962194608, target=100):
    if not APP_STORE_AVAILABLE:
        print("Skipping App Store (library not working on this machine) — collect a few reviews manually from apps.apple.com instead.")
        return []
    print(f"Fetching App Store reviews for {app_name} ...")
    collected = []
    try:
        app = AppStore(country="us", app_name=app_name, app_id=app_id)
        app.review(how_many=target * 4)  # over-fetch since we'll filter most out
        for r in app.reviews:
            content = clean(r.get("review", ""))
            if content and is_relevant(content):
                rating = r.get("rating", "")
                date = str(r.get("date", ""))[:10]
                collected.append(f"App Store review ({date}, {rating}\u2605): {content}")
    except Exception as e:
        print(f"  App Store fetch failed: {e}")
    return collected[:target]


if __name__ == "__main__":
    all_lines = []
    all_lines += collect_play_store(target=700)
    all_lines += collect_app_store(target=100)

    out_path = "google_photos_reviews_filtered.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(all_lines))

    print(f"\nDone. {len(all_lines)} relevant reviews saved to {out_path}")
    print("Open that file, review it briefly, then paste its contents into the discovery engine tool's textarea.")
