from telebot import TeleBot
import pickle

TOKEN = 'YOURTOKEN'
bot = TeleBot(token=TOKEN)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
        "🎬 Welcome to classification_positive-negative_reviews Bot! "
        "I'm here to analyze movie reviews and tell you whether the sentiment is positive 😊 or negative 😞. "
        "Just send me a movie review (real or made-up), and I’ll classify it for you instantly. "
        "Example: “This movie was a masterpiece. The story, acting, and visuals were perfect!”"
    )

@bot.message_handler()
def review(message):
    prediction = model.predict([message.text])
    sentiment = "😊 Positive" if prediction == 1 else "😞 Negative"
    bot.send_message(message.chat.id, f"Predicted sentiment: {sentiment}")

bot.polling()