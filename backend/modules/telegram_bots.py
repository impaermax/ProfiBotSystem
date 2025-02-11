def generate_telegram_bot_code(token, commands, auto_responses):
    code_template = f"""
import telebot

bot = telebot.TeleBot("{token}")

@bot.message_handler(commands={commands})
def handle_commands(message):
    command = message.text.split()[0]
    bot.reply_to(message, f"Command received: {command}")

@bot.message_handler(func=lambda message: True)
def handle_auto_response(message):
    response = {auto_responses}.get(message.text.lower(), "I don't understand")
    bot.reply_to(message, response)

bot.polling()
"""
    return code_template
