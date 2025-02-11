from flask import Flask, request, jsonify, send_file
from modules.site_analysis import analyze_website
from modules.telegram_bots import generate_telegram_bot_code
from modules.voice_bots import convert_text_to_speech

app = Flask(__name__)

# API для анализа сайта
@app.route('/api/site-analysis', methods=['POST'])
def site_analysis():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    result = analyze_website(url)
    return jsonify(result)

# API для создания Telegram-бота
@app.route('/api/telegram-bot', methods=['POST'])
def telegram_bot():
    data = request.json
    token = data.get('token')
    commands = data.get('commands', [])
    auto_responses = data.get('auto_responses', {})

    if not token:
        return jsonify({"error": "Token is required"}), 400

    bot_code = generate_telegram_bot_code(token, commands, auto_responses)
    return jsonify({"bot_code": bot_code})

# API для конвертации текста в речь
@app.route('/api/voice-bot', methods=['POST'])
def voice_bot():
    data = request.form
    text = data.get('text')
    engine = data.get('engine', 'google_tts')

    if not text:
        return jsonify({"error": "Text is required"}), 400

    audio_path = convert_text_to_speech(text, engine)
    return send_file(audio_path, as_attachment=True, mimetype='audio/mp3')

if __name__ == '__main__':
    app.run(debug=True)
