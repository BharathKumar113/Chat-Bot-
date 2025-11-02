from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from gpt4all import GPT4All

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Load GPT4All
model = GPT4All("orca-mini-3b.gguf2.Q4_0.gguf")  # lightweight model

chat_memory = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_memory[user_id] = []
    await update.message.reply_text(" Hi! I'm your offline GPT4All bot. Ask me anything!")

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_memory[user_id] = []
    await update.message.reply_text(" Memory cleared! Let's start fresh.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    if user_id not in chat_memory:
        chat_memory[user_id] = []

    chat_memory[user_id].append({"role": "user", "content": user_message})

    # Keep recent messages
    if len(chat_memory[user_id]) > 8:
        chat_memory[user_id] = chat_memory[user_id][-8:]

    # Combine chat history
    conversation = "\n".join(
        f"{m['role']}: {m['content']}" for m in chat_memory[user_id]
    )

    with model.chat_session():
        reply = model.generate(conversation, max_tokens=200)

    chat_memory[user_id].append({"role": "assistant", "content": reply})
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Offline GPT4All Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
