import time
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# configure
BOT_TOKEN = "replace with your token"

# Choose a fast Hugging Face model
HF_MODEL = "facebook/blenderbot-400M-distill"  #fast
HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
HF_HEADERS = {}  # No token needed for public models


#  Hugging Face Query Function 
def query_huggingface(prompt, retries=3):
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 150}}
    for attempt in range(retries):
        try:
            response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload, timeout=40)
            data = response.json()

            # Model still loading
            if "error" in data and "loading" in data["error"].lower():
                print("Model still loading... waiting 10s")
                time.sleep(10)
                continue

            # Parse output (some models return list, some dict)
            if isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
                return data[0]["generated_text"]

            if isinstance(data, dict) and "generated_text" in data:
                return data["generated_text"]

            return str(data)

        except Exception as e:
            print(f"Error on attempt {attempt+1}: {e}")
            time.sleep(5)

    return "Model is busy or not responding. Please try again soon."


# === Telegram Commands ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(" Hello! I’m your AI chatbot using Hugging Face.\nType anything to chat!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    await update.message.reply_text(" Thinking...")

    response = query_huggingface(user_input)
    await update.message.reply_text(response)


# === Run Bot ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print(" Telegram bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
