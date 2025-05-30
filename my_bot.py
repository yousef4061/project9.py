import random
import telebot
from telebot import types
from telebot.handler_backends import StatesGroup, State
import qrcode

class GameStares(StatesGroup):
     Waiting_for_name = State()
     Waiting_for_age = State()


class player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._voice = f"{self.name} is shouting"
        self._max = (147, 78, 158, 20)

    @property
    def voice(self):
        return self._voice

    @property
    def max(self):
        return self._max

    @property
    def argmax(self):
        return self._max

    def new_game(self):
        return f"welcome to the new game, {self.name}"


bot = telebot.TeleBot("7685139261:AAFJD2JpsyySwOXGO5tyz9H61PJZP9p2RG8")


my_keyboard = types.ReplyKeyboardMarkup(row_width=3)
key1 = types.KeyboardButton("سلام به همه")
key2 = types.KeyboardButton("خداحافظ")
key3 = types.KeyboardButton("عشقم")
key4 = types.KeyboardButton("عکس")
key5 = types.KeyboardButton("فال")
key6 = types.KeyboardButton("چت")
my_keyboard.add(key1, key2, key3, key4, key5, key6)


players = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "سلام جون دل خوش اومدی عزیز 😍")
	

@bot.message_handler(commands=["fal"])
def send_fal(message):
    fal_list = ["امروز روز خوبیه", "عشقت بهت فکر میکنه", "موفق میشی", 
                "به زودی خبر خوب میشنوی", "امروز روز خوبی برای شروع کار جدیده"]
    selected_fal = random.choice(fal_list)
    bot.send_message(message.chat.id, selected_fal)


     
@bot.message_handler(commands=["game"])
def start_game(message):
     bot.reply_to(message, f"chat ID فعلی: {message.chat.id}")
     msg = bot.reply_to(message,"لطفا اسم خودت رو وارد کن")
     bot.register_next_step_handler(msg, process_name)

def process_name(message):
         name = message.text
         bot.reply_to(message, "سن خودت رو وارد کن")
         bot.register_next_step_handler(message, process_age, name)

def process_age(message, name):
    age = int(message.text)
    if message.chat.id not in players:
        p = player(name, age)
        players[message.chat.id] = p     
        bot.send_message(message.chat.id, f"chat ID لطفا: {message.chat.id}")
        bot.send_message(message.chat.id, f"بازیکن ذخیره شد: {p.name}, {p.age}")
        bot.send_message(message.chat.id, p.new_game())
        bot.send_message(message.chat.id, f"Voice: {p.voice}")
        bot.send_message(message.chat.id, f"Max: {p.max}")
        bot.send_message(message.chat.id, f"Argmax: {p.argmax}")


@bot.message_handler(commands=['voice'])
def send_voice(message):
    if message.chat.id in players:
        player = players[message.chat.id]
        bot.reply_to(message, f"chat ID فعلی: {message.chat.id}")
        bot.send_message(message.chat.id, f"Voice: {player.voice}")
    else:
        bot.send_message(message.chat.id, "/gameطفا اول اسم و سنت رو وارد کن ل")

@bot.message_handler(command=['qrcode'])
def send_qrcode(message):
        qr = qrcode.make(f"chat ID: {message.chat.id}")
        qr.save("temp_qr.png")
        with open("temp_qr.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "این qr کد شماست")

@bot.message_handler(commands=['max'])
def send_max(message):
    if message.chat.id in players:
        player = players[message.chat.id]
        bot.reply_to(message, f"chat ID لطفا: {message.chat.id}")
        bot.send_message(message.chat.id, f"Max: {player.max}")
    else:
        bot.send_message(message.chat.id, "/game لطفا اول بازی رو شروع کن")

@bot.message_handler(commands=['argmax'])
def send_argmax(message):
    bot.reply_to(message, f"chat ID فعلی: {message.chat.id}")
    if message.chat.id in players:
        player = players[message.chat.id]
        bot.send_message(message.chat.id, f"Argmax: {player.argmax}")
    else:
        bot.send_message(message.chat.id, "/game لطفا اول اسم و سنت رو وارد کن ل")

@bot.message_handler(commands=['photo'])
def sendP_photo(message):
    if message.text == "عکس":
        bot.reply_to(message, "عکس قدی خودت")
    else:
        pgoto = open("session9/khoshgel.jpg", "rb")
        bot.send_photo(message.chat.id, pgoto)
    bot.send_message(message.chat.id, "عکس ارسال شد", reply_markup=my_keyboard)
          
@bot.message_handler(commands=['help'])
def help(message):
    help_text = """
    /start: خوش آمد گویی
    /game: وارد کردن اسم و سن برای بازی
    /fal: دریافت فال تصادفی
    /voice: voice صدای شما
    /max: max حداکثر شما
    /argmax: آرگومنت حداکثر شما
    /qrcode: QR ارسال کد
    /help: راهنما
    """
    bot.send_message(message.chat.id, help_text, parse_mode='markdown') 

@bot.message_handler(func=lambda m: True)
def send_all(message):
    if message.text == "سلام":
        bot.reply_to(message,"علیک سلام")
    elif message.text == "خوبی؟":
        bot.reply_to(message, "نه فقط توخوبی")
    elif message.text == "دوست دارم":
        bot.reply_to(message, "🧡")
    elif message.text == "عکس قدی بده":
         photo = open("session9/khoshgel.jpg", "rb")
         bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "نمیفهمم چی داری میگی😐", reply_markup=my_keyboard)


bot.infinity_polling()
