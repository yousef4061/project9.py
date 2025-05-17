# project9.py
# Simple Telegram Bpt
A straightforward Telegram bot built with Python.

## Features
    . <span style="color: red;"> /start </span>: Welcomes users.
    . <span style="color: red;"> /fal </span>: Shows a random fortune.
    . <span style="color: red;"> /game </span>: Collects name and age for a game.
    .Responds to messages like "hello everyone", "Goodbye", "My love", and sends a photo.

## Prerequisites
. Python 3.6+
. Install <span style="color: red;"> pyTelegramBotAPI</span>:

```
pip install pyTelegramBotAPI
```
## setup & Run
### 1. Setup Environment
. Create and activate a virtual environment:

```
python -m venv venv
venv\Scripts\activate #windows
```
. Install the library:

```
pip install pyTelegramBotAPI
```
### 2. Configure Bot
. Get a token from <span style="color: red;"> @botFather </span> on telegram

. Update <span style="color: red;"> telegram_bot.py </span>, line 44:

```
bot = telebot.TeleBot("your_new_token_here)
```
### 3. Run Bot
. Use VPN if in a restricted region.

. Run:

```
python telegram_bot.py
```
. Test with <span style="color: red;"> /start, /fal</span>, or <span style="color: red;"> /game</span>.

## Troubleshooting
. **ModuleNotFoundError**: Ensure <span style="color: red;"> pyTelegramBotAPI</span> is installed.

. **ConnectionError**: Enable VPN.

. **VS Code Issues**: Select the correct interpreter (. <span style="color: red;">\venv\Scripts\python.exe</span>).

### Coding Tips
. **Format Code**:

```
# Good
custom_keyboard = types.ReplyKeyboardMarkup(row_width=3)
custom_keyboard.add(key1, key2, key3)
```
. **Add Comments**:

```
#send a welcome message
bot.reply_to(message, "Welcome! 😍)
```
. **Use Constants**:

```
FORTUNE_MESSAGES = ["Today is a great day! 😄", "You'11 succeed! 👍"]
```
## notes
. Keep your token private.

. Check https://pytba.readthedocs.io/ for more features.
