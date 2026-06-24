# 🎙️ Vani – Multilingual Voice-First Customer Support Agent

> 🚀 An AI-powered multilingual voice assistant that understands Hindi, English, and Hinglish, performs customer-support actions through intelligent tool calling, and responds naturally using speech synthesis.

---

## 🌟 Project Overview

**Vani** is a next-generation Voice AI Agent designed to automate Tier-1 customer support interactions. The system enables users to communicate naturally through voice while the AI understands requests, extracts information, performs backend operations, and responds in real time.

Instead of navigating menus or waiting for human agents, customers can simply speak and receive immediate assistance.

---

## 🎯 Problem Statement

Customer support teams spend a significant amount of time handling repetitive queries such as:

📦 "Where is my order?"
🔑 "I forgot my password."
🏠 "Update my delivery address."
💳 "What is my refund status?"

Vani automates these interactions through an end-to-end conversational AI pipeline powered by Speech AI, NLP, LLMs, and Tool Calling.

---

## 🏆 Segment Information

### 📌 Segment

**Segment 3 – Applied AI & Intelligent Systems**

### 📌 Project Code

**C3 – Voice-First Customer Support: Multilingual Speech AI**

---

## ✨ Key Features

### 🎤 Speech Understanding

* Automatic Speech Recognition (ASR)
* Hindi Support 🇮🇳
* English Support 🇬🇧
* Hinglish Support 🔄

### 🧠 Natural Language Understanding

* Intent Classification (50+ Intents)
* Named Entity Recognition (NER)
* Slot Filling
* Context-Aware Conversations

### 🤖 Conversational Intelligence

* Stateful Dialog Management
* LLM-Powered Fallback Responses
* Multi-turn Conversations

### 🔧 Tool Calling & Automation

* 📦 Order Tracking
* 🔑 Password Reset
* 🏠 Address Update
* 💳 Refund Status
* 👤 Account Operations

### 🔊 Voice Generation

* Natural Text-to-Speech
* Human-like Voice Responses

### 📊 Monitoring & Reliability

* Langfuse Observability
* Conversation Tracing
* Tool Call Monitoring
* Latency Tracking
* Hallucination Prevention

### 🔒 Security & Safety

* PII Redaction
* Safe Response Generation
* Tool-Verified Information Retrieval

---

## 🏗️ System Architecture

```text
┌───────────────────┐
│   🎤 User Voice   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  🗣️ Whisper ASR   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ 🌍 Language Detect │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ 🧠 Intent + NER   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ 🤖 Dialog Manager │
│    (LangGraph)    │
└─────────┬─────────┘
          │
 ┌────────┼─────────┐
 │        │         │
 ▼        ▼         ▼
📦       🔑        🏠
Order   Reset    Address
API     API      API
 │        │         │
 └────────┼─────────┘
          │
          ▼
┌───────────────────┐
│ 💬 Response Layer │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ 🔊 XTTS Engine    │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ 🎧 Voice Response │
└───────────────────┘

📊 Monitoring: Langfuse
```

---

## 🛠️ Technology Stack

| Component                | Technology           |
| ------------------------ | -------------------- |
| 🎨 Frontend              | React + Tailwind CSS |
| ⚙️ Backend               | FastAPI              |
| 🗄️ Database             | PostgreSQL           |
| 🎤 Speech Recognition    | Whisper Large-v3     |
| 🌍 Language Detection    | LangDetect           |
| 🧠 Intent Classification | DistilBERT           |
| 🔍 Entity Extraction     | spaCy + Regex        |
| 🤖 Dialog Manager        | LangGraph            |
| 💡 LLM Fallback          | Gemini API           |
| 🔊 Text-to-Speech        | XTTS v2              |
| ☎️ Telephony             | Twilio               |
| 📊 Observability         | Langfuse             |
| 📈 Evaluation            | DeepEval             |
| 🐳 Containerization      | Docker               |
| ☁️ Deployment            | AWS / Render         |
| 🔬 Experiment Tracking   | Weights & Biases     |
| 🧪 Testing               | Pytest               |

---

## 📋 Evaluation Strategy

The system will be evaluated using:

✅ 100 Multilingual Test Calls
✅ Intent Accuracy
✅ Entity Extraction F1 Score
✅ Task Success Rate
✅ Average Handle Time
✅ End-to-End Pipeline Validation
✅ Hallucination Detection Rate

---

## 🎯 Target Roles

* 🤖 AI Engineer
* 🧠 Machine Learning Engineer
* 💬 Conversational AI Engineer
* 📚 NLP Engineer
* ⚡ Applied AI Engineer
* 🚀 Generative AI Engineer

---

## 👨‍💻 Developer

### Shivam Kumar

Building intelligent voice systems that bridge the gap between humans and AI through natural conversations.


> 💡 *"Talk naturally. Let AI handle the rest."*
