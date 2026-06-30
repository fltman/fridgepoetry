# Fridge Poetry

[![Support me on Patreon](https://img.shields.io/badge/Patreon-Support%20my%20work-FF424D?style=flat&logo=patreon&logoColor=white)](https://www.patreon.com/AndersBjarby)

An AI-assisted fridge-magnet poetry web app. Each visit, GPT generates a fresh set of ~100 varied words (nouns, verbs, adjectives, and so on) scattered on a virtual fridge door. Drag the magnets into sentences — and let the AI suggest the next word to extend the line you're building.

## What it does

- On load, asks the OpenAI API for 100 random, grammatically varied words and renders them as draggable magnets (`GET /`).
- `POST /construct` takes your available words plus the sentence so far and asks GPT to pick one word from the list to extend it.

## Setup

Requires Python 3 and an OpenAI account:

```bash
pip install flask openai
export OPENAI_API_KEY=sk-...
python3 app.py
```

The Flask dev server starts on http://localhost:5000.

## Tech

Python + Flask backend, OpenAI GPT (chat completions), HTML/JS frontend (`templates/index.html`).
