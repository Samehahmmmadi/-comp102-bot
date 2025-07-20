import os
from flask import Flask, request
import telebot
from telebot import types

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("⚠️ متغير البيئة TELEGRAM_TOKEN غير موجود. الرجاء إضافته في إعدادات Render.")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# --- قوائم الردود (نفس قوائمك) ---
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("1️⃣ تخصصات برامج الدبلوم - حضوري", "2️⃣ تخصصات برامج الدبلوم - عن بعد")
    markup.row("3️⃣ قناة وإعلانات الدبلوم", "4️⃣ خدمات حل الواجبات والبحوث")
    markup.row("5️⃣ مواقع فروع جامعة الملك سعود", "6️⃣ التجسير", "7️⃣ شرح البلاك بورد")
    return markup

def حضوري_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("دبلوم محاسبة", "دبلوم التسويق", "دبلوم الأنظمة")
    # ... باقي القائمة ...
    markup.row("🔙 رجوع")
    return markup

def عن_بعد_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("شرح - البلاك بورد / Blackboard")
    markup.row("دبلوم الإدارة المالية والمصرفية - عن بعد")
    markup.row("🔙 BACK")
    return markup

# --- handlers ---
@bot.message_handler(commands=['start'])
def start_handler(message):
    text = (
        "◆ اضغط على الأوامر في القائمة في الأسفل وتطلع لك كل تفاصيل الدبلوم\n\n"
        "📣 قناة مساعدات طلاب الدبلوم:\n"
        "[اضغط هنا للدخول إلى القناة](https://t.me/Aoun_Academic)"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu())

@bot.message_handler(func=lambda m: True)
def menu_handler(message):
    text = message.text.strip()
    if text in ["🔙 رجوع", "🔙 BACK"]:
        bot.send_message(message.chat.id, "تم الرجوع إلى القائمة الرئيسية ✅", reply_markup=main_menu())
    elif text == "1️⃣ تخصصات برامج الدبلوم - حضوري":
        bot.send_message(message.chat.id, "اختر أحد تخصصات الدبلوم الحضوري:", reply_markup=حضوري_menu())
    elif text == "2️⃣ تخصصات برامج الدبلوم - عن بعد":
        bot.send_message(message.chat.id, "اختر أحد تخصصات الدبلوم عن بعد:", reply_markup=عن_بعد_menu())
    # ... أكمل باقي الخيارات كما في كودك ...
    else:
        bot.send_message(message.chat.id, "❗الأمر غير معروف، الرجاء استخدام القائمة.")

# --- استقبال التحديثات من Telegram عبر Webhook ---
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

# --- مسار لفحص حالة السيرفر ---
@app.route('/')
def index():
    return "Bot is alive!", 200

if __name__ == '__main__':
    # ازالة أي webhook سابق
    bot.remove_webhook()
    # تعيين webhook على الرابط الحقيقي
    WEBHOOK_URL = f"https://YOUR_DOMAIN_HERE/{TOKEN}"  # غيره برابط موقعك مع https
    bot.set_webhook(url=WEBHOOK_URL)

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
