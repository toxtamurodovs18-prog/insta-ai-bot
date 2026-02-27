import telebot
import openai

BOT_TOKEN = "8545760470:AAFCqNjax9Ty2VoCbaYNtufbRQ5DWAM9BU0"
OPENAI_KEY = "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"

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_KEY

@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":message.text}],
            temperature=0.7
        )
        answer = response['choices'][0]['message']['content']
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {e}")

bot.infinity_polling()
