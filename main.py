import os
from flask import Flask, request
import telebot
from telebot import types

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("⚠️ متغير البيئة TELEGRAM_TOKEN غير موجود. الرجاء إضافته في إعدادات Render.")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# -- قائمة الأوامر على اليسار --
left_commands = ["star", "help"]

# --- قائمة يمين البوت: التبويبات 1 إلى 10 ---
right_tabs = [
    "تقويم عام 1447ه‍.",
    "خدمات التواصل مع الجامعة",
    "الاسئلة الشائعة_عام",
    "تخصصات برامج الدبلوم - حضوري",
    "تخصصات برامج الدبلوم - عن بُعد",
    "قناة وإعلانات الدبلوم 📢",
    "خدمات حل الواجبات وعمل المشاريع والبحوث",
    "مواقع فروع جامعة الملك سعود",
    "شروط التجسير في جامعة الملك سعود",
    "🛑شرح استخدام – البلاك بورد / Blackboard 🛑"
]

# --- رسالة ترحيب عند /start ---
@bot.message_handler(commands=['start'])
def start_handler(message):
    text = (
        "🔹 *ما الذي يمكن لهذا البوت تقديمه؟*\n\n"
        "هذا البوت مُخصص لطلاب *الدبلوم في جامعة الملك سعود*، ويهدف إلى:\n\n"
        "✅ *توفير المعلومات الدراسية بسهولة وسرعة*\n"
        "✅ *مساعدة الطالب في الوصول لكل ما يحتاجه من روابط ومصادر مهمة*\n"
        "✅ *تقليل الوقت والجهد المبذول في البحث*\n"
        "✅ *تجميع كل ما يهم الطالب في مكان واحد*\n\n"
        "نأمل أن تكون هذه الخدمة عند حسن ظنكم،\n"
        "ونسعد دائمًا بخدمتكم 💙\n"
        "*جزيل الشكر والتقدير لكم 🌹*\n\n"
        "قناة مساعدات طلاب الدبلوم 👇\n"
        "https://t.me/Diploma_Solutions"
    )
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # نضع الأوامر على اليسار
    markup.row(*left_commands)
    # نضع التبويبات في قائمة عمودية - كل تبويب في صف
    for tab in right_tabs:
        markup.add(tab)
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

# --- التعامل مع أوامر اليسار (star, help) ---
@bot.message_handler(func=lambda m: m.text in left_commands)
def left_command_handler(message):
    text = message.text
    if text == "star":
        reply = (
            "اضغط على الأوامر الموجودة في القائمة (قائمة في يمين البوت) أدناه لتحصل على كل ما تحتاجه:\n\n"
            "🎯 نأمل أن تنال خدمتنا رضاكم وأن نكون عند حسن ظنكم…"
        )
    elif text == "help":
        reply = "فيديو #شــــــرح_استخدام_البوت سيتوفر قريبا"
    bot.send_message(message.chat.id, reply)

# --- التعامل مع التبويبات في يمين البوت ---
@bot.message_handler(func=lambda m: m.text in right_tabs)
def right_tab_handler(message):
    text = message.text

    if text == "تقويم عام 1447ه‍.":
        reply = "التقويم الدراسي للعام الجامعي 1447هـ في جامعة الملك سعود لم يُنشر بشكل رسمي بعد"
        bot.send_message(message.chat.id, reply)

    elif text == "خدمات التواصل مع الجامعة":
        reply = (
            "عمادة السنة الأولى المشتركة\n"
            "SSHELP@CFY.KSU.EDU.SA\n"
            "00966-114694006\n\n"
            "الشؤون الطلابية\n"
            "ksugcc@ksu.edu.sa\n"
            "00966 1 8050141\n\n"
            "المشرف على وحدة التوجيه والإرشاد الطلابي\n"
            "sg@cfy.ksu.edu.sa\n"
            "4694118\n"
            "رقم المكتب: 2484\n\n"
            "المشرف على وحدة شؤون الطلاب\n"
            "sa@cfy.ksu.edu.sa\n\n"
            "إيميلات عمادة القبول والتسجيل\n"
            "dar@ksu.edu.sa\n"
            "darweb@ksu.edu.sa\n\n"
            "أرقام عمادة القبول والتسجيل\n"
            "0114677722\n"
            "0118054402\n\n"
            "منسق/ة الفيزياء\n"
            "nbennessib@ksu.edu.sa\n"
            "nalkathran@ksu.edu.sa\n\n"
            "منسق أحياء\n"
            "aalii@ksu.edu.sa\n"
            "somer@ksu.edu.sa\n\n"
            "منسق كيم\n"
            "amenizi@ksu.edu.sa\n"
            "zalmarhoon@ksu.edu.sa\n\n"
            "منسق/ة إنجل\n"
            "mramadan@cfy.ksu.edu.sa\n"
            "h.alshareef@cfy.ksu.edu.sa\n\n"
            "فرع عليشة (بنات)\n"
            "011 805 7331\n\n"
            "فرع الناصرية (الوشم بمسمى آخر)\n"
            "0114036600"
        )
        bot.send_message(message.chat.id, reply)

    # تابع باقي الأوامر هنا كما هو مذكور في الكود الأصلي

# --- Webhook for Flask ---
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route('/')
def webhook():
    # نزيل أي Webhook قديم ونقوم بتعيين Webhook جديد
    bot.remove_webhook()
    bot.set_webhook(url='https://kingsauddiploma-bot.onrender.com/' + TOKEN)
    return "Webhook set", 200

if __name__ == '__main__':
    # تعيين الـ Webhook عند بدء التشغيل
    bot.remove_webhook()
    bot.set_webhook(url='https://kingsauddiploma-bot.onrender.com/' + TOKEN)

    # تشغيل تطبيق Flask
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    
