# Photo Retrieval Discovery Engine

An AI-powered tool that reads real user complaints (Play Store reviews, App Store reviews, Reddit threads, forum posts, community discussions) about failing to find an old photo in Google Photos, and sorts them into concrete failure patterns — instead of just doing sentiment analysis.

**Public findings page — test/view this one, no login ever needed:**
https://sanbhati07.github.io/Discovery-Engine/

This shows the real result from analyzing 250 collected Play Store reviews, with evidence and methodology notes. This is the link to use for reviewing this project.

*(Optional, secondary: [an interactive live version](https://claude.ai/artifact/Nd764ScX8F5d6MthGM21cF) exists where you can paste your own reviews and get a fresh AI analysis in real time — but it requires a free Claude.ai account, so it isn't the primary link for this submission.)*

## What's in this repo

| File | What it is |
|---|---|
| `index.html` | The public findings page (this is what's running at the link above) |
| `discovery-engine.html` | Source code of the interactive live-AI version |
| `collect_reviews.py` | A script to pull real, relevant reviews from the Play Store and App Store, so you don't have to copy-paste them by hand |
| `README.md` | This file |

## Why this exists

Google Photos users often remember *something* about an old photo — a place, an event, a rough date, a person — but not enough to type a search that actually finds it. This tool exists to answer, with real evidence rather than guesswork:

- What kinds of photos do people struggle to find again?
- What do they actually remember, and what have they forgotten?
- Where exactly does the search experience break down — not finding the words, the search misunderstanding a clue, too many/unclear results, or just not trusting the AI search feature enough to use it?

## How it works

Every comment gets classified against a fixed 5-stage "retrieval journey" model:

1. **Expressing** — can't put the memory into words at all
2. **Understanding** — gave a real clue, but the search didn't use it correctly
3. **Judging** — got results back, but can't tell which one is right
4. **Recovering** — first search failed, no good way to refine it
5. **Trusting** — an AI search feature exists, but the person avoids or distrusts it

Each comment is also tagged with the type of photo involved and, where mentioned, exactly what the person remembered vs. what they'd forgotten. Similar comments across a large batch get grouped into named themes with the original evidence attached, so nothing is invented or assumed.

## How to add your own data

1. Install the review-scraping library once:
