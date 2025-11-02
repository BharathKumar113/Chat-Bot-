from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI

#configure keys
BOT_TOKEN = " Replace this with your key""
OPENAI_API_KEY = " Replace this with your key"

# START OPENAI CLIENT 
client = OpenAI(api_key=OPENAI_API_KEY)

# CHAT MEMORY STORAGE 
chat_memory = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_memory[user_id] = []
    await update.message.reply_text(" Hi! I'm your AI bot with memory. Let's chat!")

# /reset command to clear memory
async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_memory[user_id] = []
    await update.message.reply_text(" Memory cleared! Let's start fresh.")

# Handle text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    # Create memory if new user
    if user_id not in chat_memory:
        chat_memory[user_id] = []

    # Append user message to memory
    chat_memory[user_id].append({"role": "user", "content": user_message})

    # Keep only last 10 messages per user
    if len(chat_memory[user_id]) > 10:
        chat_memory[user_id] = chat_memory[user_id][-10:]

    try:
        # Send message + history to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_memory[user_id]
        )

        # Extract bot reply
        ai_reply = response.choices[0].message.content

        # Add reply to memory
        chat_memory[user_id].append({"role": "assistant", "content": ai_reply})

        await update.message.reply_text(ai_reply)

    except Exception as e:
        await update.message.reply_text(f" Error: {str(e)}")

# --- MAIN FUNCTION ---
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print(" AI Telegram Bot with memory is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
