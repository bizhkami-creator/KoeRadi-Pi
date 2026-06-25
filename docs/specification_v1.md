
# KoeRadi Pi v1.0 Specification

## Project

KoeRadi Pi

## Goal

Raspberry Pi上で動作する音声操作ラジオプレーヤー

対象：
・視覚障害者
・高齢者
・ラジオヘビーユーザー

---

# Hardware

- Raspberry Pi 5
- Raspberry Pi OS
- Jabra Speak 510
- Wi-Fi

---

# Software

Python

mpv

Whisper/Vosk

Gemini Flash Lite

---

# Version 1.0

## 音声操作

ヨッシー

↓

待機

↓

コマンド受付

---

## ライブ再生

「TBSつけて」

「文化放送」

「FM東京」

---

## 再生操作

止めて

続けて

音量上げて

音量下げて

ミュート

---

## タイムフリー

昨日の〇〇

一昨日の〇〇

○日前の〇〇

---

## ローカル再生

Google Drive同期済み録音

ローカル保存済み録音

---

# Player Architecture

Voice

↓

Command Parser

↓

Player API

↓

Radiko Engine

Local Engine

Drive Engine

---

# Future

Podcast

Audible

YouTube Audio

Spotify

Bluetooth Speaker

