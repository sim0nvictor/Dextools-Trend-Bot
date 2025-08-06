from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import os

TOKEN = os.getenv("8366044785:AAEV4HkJPS-i6q3tVZuR0YdsLS_zQoMshHg")

def start(update: Update, context: CallbackContext):
    buttons = [
        [InlineKeyboardButton("Start Pumping 🚀", callback_data='start_pump')],
        [InlineKeyboardButton("Premium Trending ✅", callback_data='premium')],
        [InlineKeyboardButton("Volume Booster 🔵", callback_data='volume')],
        [InlineKeyboardButton("Transaction Booster 🔵", callback_data='transaction')],
        [InlineKeyboardButton("Deposit 💸", callback_data='deposit'),
         InlineKeyboardButton("My Wallet 👛", callback_data='wallet')],
        [InlineKeyboardButton("DASHBOARD 🧾", callback_data='dashboard')],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("👋 Welcome to SEV's Pump Bot!\nChoose an option below:", reply_markup=reply_markup)

def handle_button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"You clicked: {query.data}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_button))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
