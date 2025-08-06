# Reviews Telegram Bot 🎬😊😞✨

Welcome to the **Reviews Telegram Bot**! 🎉 This super cool Telegram bot analyzes movie reviews and predicts whether the sentiment is positive 😊👍 or negative 😞👎 using a powerful machine learning model! 🤖 Built with Python and powered by a pre-trained XGBoost classifier, it’s your go-to buddy for quick movie review insights! 🍿🔥

## 🚀🌟 Features

- **Instant Sentiment Magic** 🪄: Send a movie review, and get a positive 😊 or negative 😞 prediction in a snap!
- **Super Simple to Use** 😎: Just type `/start` and toss in a review.
- **Machine Learning Awesomeness** 🧠: Trained on the IMDB Dataset with XGBoost for top-notch accuracy.
- **Lightweight & Fun** ⚡: Minimal setup, maximum fun with emoji-filled responses! 🎈

## 📂 Project Structure

- `bot.py` 📜: The main Telegram bot script that chats with users and loads the model.
- `Reviews.ipynb` 📓: Jupyter notebook with all the data preprocessing, model training, and `model.pkl` creation.
- `model.pkl` 💾: The pre-trained XGBoost model for sentiment predictions.

## 🛠️✨ Installation

1. **Clone the Repo** 🖥️:
   ```bash
   git clone https://github.com/your-username/Reviews_telegram_bot.git
   cd Reviews_telegram_bot
   ```

2. **Install the Goodies** 📦:
   You’ll need these Python libraries:
   - `python-telegram-bot` 🤖
   - `scikit-learn` 📊
   - `xgboost` 🚀
   - `pandas` 🐼
   - `numpy` 🔢

   Install them with:
   ```bash
   pip install python-telegram-bot scikit-learn xgboost pandas numpy
   ```

3. **Set Up Your Telegram Bot** 📲:
   - Chat with [BotFather](https://t.me/BotFather) on Telegram to grab your `TOKEN` 🔑.
   - Pop that `TOKEN` into `bot.py` where it says `TOKEN`.

4. **Launch the Bot** 🚀:
   ```bash
   python bot.py
   ```

## 🧠🔍 How It Works

1. **Data Prep Magic** 🪄:
   - The `Reviews.ipynb` notebook loads the IMDB Dataset 📚, turns sentiments into 0 (negative 😞) or 1 (positive 😊), and uses `TfidfVectorizer` to make text machine-readable. 🤓
   - `GridSearchCV` tunes the XGBoost model to perfection, saving it as `model.pkl`. 💾

2. **Bot Action** 🎭:
   - Uses `python-telegram-bot` to chat with you! 💬
   - `/start` kicks things off with a fun intro. 🎬
   - Send any text review, and the bot predicts its vibe! 😄

3. **Prediction Power** ⚡:
   - Loads `model.pkl` and analyzes your review. 📈
   - Returns a sentiment with emojis: 😊👍 for positive, 😞👎 for negative.

## 🎮🎉 Usage

1. Fire up the bot with `/start` in Telegram. 🚀
2. Send a movie review like: "This movie was epic! Mind-blowing story and visuals! 🎥🔥"
3. Get a response like: "Predicted sentiment: 😊 Positive 👍"

## 📊🤖 Model Details

- **Dataset** 📚: IMDB Dataset with 50,000 movie reviews! 🎬
- **Model** 🧠: XGBoost classifier with `TfidfVectorizer` for text processing.
- **Tuning** ⚙️: `GridSearchCV` with `max_depth=7` and `n_estimators` from 100 to 300.
- **Output** 📢: Binary classification (0 = Negative 😞, 1 = Positive 😊).

## 🖼️🌈 Example

**User Input** 🎤:
> This movie was a masterpiece! The story, acting, and visuals were perfect! 🌟

**Bot Response** 💬:
> Predicted sentiment: 😊 Positive 👍✨

**User Input** 🎤:
> The plot was dull, and the characters were so flat. 😴

**Bot Response** 💬:
> Predicted sentiment: 😞 Negative 👎

## 📝✨ Notes

- Keep `model.pkl` in the same folder as `bot.py` or the bot will sulk! 😣
- Stick to text reviews—non-text inputs might confuse it. 🤔
- Trained on English reviews, so non-English ones might get quirky results. 🌍
- No `requirements.txt` yet, but the dependency list above has you covered! ✅

## 🤝💡 Contributing

Love to have you aboard! 🚢
- Spot a bug or have a cool idea? Open an [issue](https://github.com/your-username/Reviews_telegram_bot/issues)! 🐞
- Want to add features? Send a pull request! 🚀

## 📜 License

This project is under the MIT License. Check the [LICENSE](LICENSE) file for details. 📄

## 📬📲 Contact

Got questions or ideas? Hit us up on [GitHub Issues](https://github.com/your-username/Reviews_telegram_bot/issues) or chat with the bot on Telegram! 💬

Happy reviewing, movie buffs! 🎥🍿✨