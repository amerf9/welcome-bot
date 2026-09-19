import os
from flask import Flask
from threading import Thread
import telebot

TOKEN = "8718734827:AAF"API: AAEpd0TRlrEm0OwvzZGwsJ9JWnIG8GWss2M
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    for m in message.new_chat_members:
        bot.send_message(message.chat.id, f"نورت الجروب يا {m.first_name} 🌟❤️")

app = Flask('')
@app.route('/')
def home():
    return "Bot is running"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
Thread(target=run).start()

bot.infinity_polling()
