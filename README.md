# 🤖 Chatbot — AI Telegram Bot (Online + Offline)

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram" alt="Telegram">
  <img src="https://img.shields.io/badge/OpenAI-ChatGPT-green?logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/HuggingFace-Model-orange?logo=huggingface" alt="Hugging Face">
  <img src="https://img.shields.io/badge/GPT4All-Offline-yellow?logo=github" alt="GPT4All">
</div>

---

### 🧠 A powerful Telegram chatbot that runs with:
- 🌐 **OpenAI GPT** for cloud-based responses  
- 🤗 **Hugging Face models** for free, fast responses  
- 💻 **GPT4All** for completely offline chatting  

> Built with Python, memory support, and async Telegram Bot API.

---

##  Preview

Example:
```
/start  
Hi! I'm your AI bot. Let's chat!
```

---

## ✨ Features

✅ **Three Chat Modes**
- **OpenAI Mode:** Smart cloud responses (GPT-3.5 / GPT-4)  
- **Hugging Face Mode:** Free chatbot using BlenderBot or DialoGPT  
- **GPT4All Mode:** Offline local LLM model with zero internet usage  

✅ **Memory System**
- Bot remembers the last few messages per user  
- `/reset` command clears chat memory  

✅ **Lightweight & Modular**
- Runs on low-end systems  
- Each file is a separate backend  

---

## 📁 Project Structure
```
chatbot/
├── bot.py          # Telegram bot using OpenAI GPT API
├── huggingface.py     # Telegram bot using Hugging Face inference API
├── offline_gpt.py         # Offline Telegram bot using GPT4All
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/BharathKumar113/Chat-Botot.git
cd Chat-Bot
```

### 2️⃣ Install Dependencies
```bash
pip install python-telegram-bot openai requests gpt4all
```

### 3️⃣ Set Up Tokens
Edit each file to include your keys:
```python
BOT_TOKEN = "your_telegram_bot_token"
OPENAI_API_KEY = "your_openai_api_key"
HF_HEADERS = {"Authorization": "Bearer your_huggingface_token"}
```

> Get your Telegram token from [@BotFather](https://t.me/BotFather).

---

## 🚀 Run the Bot

### 🧩 OpenAI Version
```bash
python openai_bot.py
```

### 🤗 Hugging Face Version
```bash
python huggingface_bot.py
```

### 💻 GPT4All (Offline) Version
Download models from [gpt4all.io/models](https://gpt4all.io/models/).  
Then run:
```bash
python gpt4all_bot.py
```

---

## ⚡ Command List
| Command | Description |
|----------|--------------|
| `/start` | Start chatting |
| `/reset` | Clear memory |
| Text | Send message to chat |

---

## 🧩 Model Comparison

| Mode | Model Example | Speed | Internet Required | Memory | Cost |
|------|----------------|-------|------------------|---------|------|
| 🧠 OpenAI | `gpt-3.5-turbo` | ⚡ Fast | ✅ Yes | Cloud | 💲 Paid API |
| 🤗 Hugging Face | `facebook/blenderbot-400M` | ⚡ Medium | ✅ Yes | None | ✅ Free |
| 💻 GPT4All | `orca-mini-3b.gguf` | ⚙️ Local | ❌ No | 4–8GB RAM | 🆓 Offline |

---

## 🧠 Memory Handling
Remembers last 8–10 messages per user.  
Use `/reset` to start fresh anytime.

---

## 💡 Future Improvements
- 🗣 Voice mode (speech ↔ text)
- 💾 Persistent memory (SQLite)
- 🌍 Web dashboard for logs
- 🔁 Auto switch between AI backends

---

## 🛠 Built With
- [Python 3.10+](https://www.python.org/)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [OpenAI API](https://platform.openai.com/)
- [Hugging Face Inference API](https://huggingface.co/)
- [GPT4All](https://gpt4all.io/)

---

## 👨‍💻 Author
**Bharath Kumar**  
💬 AI enthusiast | Full Stack Developer | Ethical Hacking Learner  

---

## 📜 License
— free for use, modification & distribution.

---

<div align="center">
⭐ Star this repo if you like it — built with ❤️ by Bharath Kumar
</div>
