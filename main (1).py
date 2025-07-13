
import os
import telebot

# Legge il token dalla variabile d'ambiente
TOKEN = os.getenv("TOKEN")

# Verifica che il token esista
if TOKEN is None:
    raise ValueError("❌ TOKEN mancante! Assicurati che la variabile d'ambiente 'TOKEN' sia impostata.")

bot = telebot.TeleBot(TOKEN)

# Comando base per testare se il bot funziona
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "✅ Bot attivo e funzionante!")

# Avvia il bot
bot.polling()
