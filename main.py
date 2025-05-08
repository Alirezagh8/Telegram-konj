import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"سلام {update.effective_user.first_name}! من همیشه آنلاینم 😊")

TOKEN = os.getenv("TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

start_handler = CommandHandler("start", start)
app.add_handler(start_handler)

app.run_polling()
