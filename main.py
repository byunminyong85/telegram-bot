import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("TG_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Render 무료 서버에서 작동 중입니다 🚀")

def main():
    if not TOKEN:
        print("❌ TG_TOKEN 환경변수가 비어 있습니다.")
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ 봇이 시작되었습니다.")
    app.run_polling()

if __name__ == "__main__":
    main()
