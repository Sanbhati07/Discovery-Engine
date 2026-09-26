# Photo Retrieval Discovery Engine

An AI-powered tool that reads real user complaints (Play Store reviews, App Store reviews, Reddit threads, forum posts, community discussions) about failing to find an old photo in Google Photos, and sorts them into concrete failure patterns — instead of just doing sentiment analysis.

**Live, working tool (test it here, no login needed):**
https://claude.ai/artifact/Nd764ScX8F5d6MthGM21cF

## What's in this repo

| File | What it is |
|---|---|
| `discovery-engine.html` | Source code of the tool (this is what's running at the live link above) |
| `collect_reviews.py` | A script to pull real, relevant reviews from the Play Store and App Store, so you don't have to copy-paste them by hand |
| `README.md` | This file |

## Why this exists

Google Photos users often remember *something* about an old photo — a place, an event, a rough date, a person — but not enough to type a search that actually finds it. This tool exists to answer, with real evidence rather than guesswork:

- What kinds of photos do people struggle to find again?
- What do they actually remember, and what have they forgotten?
- Where exactly does the search experience break down — not finding the words, the search misunderstanding a clue, too many/unclear results, or just not trusting the AI search feature enough to use it?

## How it works

Every comment you feed it gets classified against a fixed 5-stage "retrieval journey" model:

1. **Expressing** — can't put the memory into words at all
2. **Understanding** — gave a real clue, but the search didn't use it correctly
3. **Judging** — got results back, but can't tell which one is right
4. **Recovering** — first search failed, no good way to refine it
5. **Trusting** — an AI search feature exists, but the person avoids or distrusts it

Each comment is also tagged with the type of photo involved and, where mentioned, exactly what the person remembered vs. what they'd forgotten. Similar comments across a large batch get grouped into named themes with the original evidence attached, so nothing is invented or assumed.

Large sets (hundreds of comments) are processed in batches of 25 automatically and then merged.

A **saved database** inside the tool lets you build up your review collection over multiple sessions instead of losing everything on refresh, and a **cached example output** button shows a real result instantly with no live AI call — so the tool is always demonstrable even if a live call is ever rate-limited.

## How to add your own data

1. Install the two review-scraping libraries once:
   ```
   pip install google-play-scraper app-store-scraper
   ```
2. Run the collector script on your own machine (needs normal internet access):
   ```
   python collect_reviews.py
   ```
   This produces `google_photos_reviews_filtered.txt` — real reviews, already filtered down to ones that actually mention search/finding/remembering.
3. Also manually collect a batch from Reddit (r/GooglePhotos, r/GooglePixel), the Google Photos Community forum, and YouTube comments on videos about the "Ask Photos" feature — search for terms like "can't find", "search doesn't work", "Ask Photos".
4. Open the live tool link above, paste everything into the box, click **Save current lines to database** so it's not lost, then **Run live analysis**.

## A note on how this is hosted

The live link above only works inside Claude's artifact viewer, because the AI analysis and the saved database both run through Claude's own infrastructure rather than a server this repo controls. This repo holds the source for transparency and technical review — for actually testing the working tool, use the live link.

## Key finding so far

Google already ships a conversational "describe what you remember" search feature (Ask Photos, launched 2024). The real, evidence-backed gap isn't the absence of natural-language search — it's that real users don't trust or fully adopt it yet, and are reverting to old keyword search habits. That reframes the opportunity from "build vague search" to "make AI-assisted retrieval something people actually rely on."
