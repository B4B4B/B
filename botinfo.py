import requests
import telebot
from telebot import types

tk = "5571315977:AAG7UZIUAAHqst4EkR-u7W3J4ApUn_d2hxE"
bot = telebot.TeleBot(tk)
@bot.message_handler(commands=['start'])
def s(message):
    cc = types.InlineKeyboardMarkup()
    b = types.InlineKeyboardButton(text="معلومات التوكن",callback_data="bs")
    cc.add(b)
    bot.send_message(message.chat.id,"اهلا بك في بوت معلومات التوكن\nاضغط على زر معلومات التوكن\nوارسل توكنك للحصول على جميع المعلومات \nDev : @K_8_U",reply_markup=cc)

@bot.callback_query_handler(func=lambda m:True)
def s(call):
    if call.message:
        if call.data == "bs":
            bot.register_next_step_handler(call.message,mm)
            bot.send_message(call.message.chat.id,"ارسل التوكن الان :")
def mm(message):
    token = message.text
    try:
        url = "https://api.telegram.org/bot"+token+"/getme"
        uel = "https://api.telegram.org/bot"+token+"/getwebhookinfo"
        r = requests.get(url).json()
        re = requests.get(uel).json()
        usl = re['result']['url']
        idu = r['result']['id']
        fs = r['result']['first_name']
        us = r['result']['username']
        bot.send_message(message.chat.id,f"""
⌯ مـعـلـومـات الـتـوكـن :
━━━━━━━━━━━━━
• مـعـرف الـبـوت : @{us} ⭐
• ايـدي الـبـوت : {idu} ❄️
• اسـم الـبـوت : {fs} 🔥
• رابـط الـمـلـف : {usl}] ⚡
━━━━━━━━━━━━━
    """)
    except:
        bot.send_message(message.chat.id,"التوكن غلط")
bot.polling()