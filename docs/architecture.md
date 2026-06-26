# AI Speaker Architecture

## Goal

Create an AI home speaker running on Raspberry Pi.

The AI should:
- Have natural conversations
- Execute skills (radio, weather, calendar...)
- Be extensible

---

## Architecture

Microphone
        │
        ▼
 Assistant
        │
        ▼
 Gemini Live API
        │
        ▼
 Intent Detection
        │
 ┌──────┴───────────┐
 ▼                  ▼
 Conversation      Skills
                      │
      ┌───────────────┼──────────────┐
      ▼               ▼              ▼
   Radio          Weather       Calendar

---

## Principles

Gemini = Brain

Raspberry Pi = Hands

Skills = Functions

Assistant = Orchestrator

# KoeRadi AI Speaker Architecture

## Goal

KoeRadi Pi is evolving from a voice-controlled radio player into an AI home speaker.

The first goal is to create an assistant that can naturally talk with the user through a microphone and speaker.

Radio playback will be added later as one of the assistant skills.

---

## Core Concept

Gemini is the brain.

Raspberry Pi is the body.

Skills are tools.

The assistant decides what the user wants, then either replies naturally or calls a skill.

---

## System Architecture

```text
Microphone
    ↓
Audio Recorder
    ↓
Assistant
    ↓
Gemini Live API
    ↓
Audio Player
    ↓
Speaker

Assistant
    ↓
Intent Detection
    ↓
Skills
    ├── Radio
    ├── TimeFree
    ├── Local Recordings
    ├── Weather
    ├── Calendar
    └── Home Assistant
