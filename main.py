import os
from flask import Flask, request
import telebot
from telebot import types

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("⚠️ متغير البيئة TELEGRAM_TOKEN غير موجود. الرجاء إضافته في إعدادات Render.")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# أوامر على اليسار
left_commands = ["star", "help"]

# التبويبات الرئيسية على اليمين
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

# ترحيب عند /start
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
    markup.row(*left_commands)
    for tab in right_tabs:
        markup.add(tab)
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

# أوامر اليسار
@bot.message_handler(func=lambda m: m.text in left_commands)
def left_command_handler(message):
    if message.text == "star":
        reply = "اضغط على الأوامر الموجودة في القائمة (قائمة في يمين البوت) أدناه لتحصل على كل ما تحتاجه:\n\n🎯 نأمل أن تنال خدمتنا رضاكم وأن نكون عند حسن ظنكم…"
    elif message.text == "help":
        reply = "فيديو #شــــــرح_استخدام_البوت سيتوفر قريبا"
    bot.send_message(message.chat.id, reply)

# التبويبات الرئيسية
@bot.message_handler(func=lambda m: m.text in right_tabs)
def right_tab_handler(message):
    text = message.text

    if text == "تقويم عام 1447ه‍.":
        bot.send_message(message.chat.id, "التقويم الدراسي للعام الجامعي 1447هـ في جامعة الملك سعود لم يُنشر بشكل رسمي بعد")

    elif text == "خدمات التواصل مع الجامعة":
        reply = (
            "عمادة السنة الأولى المشتركة:\n"
            "• SSHELP@CFY.KSU.EDU.SA\n• 00966-114694006\n\n"
            "الشؤون الطلابية:\n"
            "• ksugcc@ksu.edu.sa\n• 00966 1 8050141\n\n"
            "وحدة التوجيه والإرشاد:\n"
            "• sg@cfy.ksu.edu.sa\n• 4694118\n• المكتب: 2484\n\n"
            "وحدة شؤون الطلاب:\n"
            "• sa@cfy.ksu.edu.sa\n\n"
            "عمادة القبول والتسجيل:\n"
            "• dar@ksu.edu.sa\n• darweb@ksu.edu.sa\n• 0114677722 / 0118054402\n\n"
            "منسقي المواد:\n"
            "• فيزياء: nbennessib@ksu.edu.sa / nalkathran@ksu.edu.sa\n"
            "• أحياء: aalii@ksu.edu.sa / somer@ksu.edu.sa\n"
            "• كيم: amenizi@ksu.edu.sa / zalmarhoon@ksu.edu.sa\n"
            "• إنجل: mramadan@cfy.ksu.edu.sa / h.alshareef@cfy.ksu.edu.sa\n\n"
            "الفروع:\n"
            "• عليشة: 011 805 7331\n• الناصرية: 0114036600"
        )
        bot.send_message(message.chat.id, reply)

    elif text == "الاسئلة الشائعة_عام":
        reply = (
            "● الأسئلة الشائعة:\n\n"
            "◇ القبول:\nhttps://dar.ksu.edu.sa/ar/FAQ\n\n"
            "◇ الطلاب المنتظمين:\nhttps://dar.ksu.edu.sa/ar/faqs\n\n"
            "◇ الخريجين:\nhttps://dar.ksu.edu.sa/ar/gfaq"
        )
        bot.send_message(message.chat.id, reply)

    elif text == "تخصصات برامج الدبلوم - حضوري":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("دبلوم محاسبة")
        markup.row("🔙 رجوع")
        bot.send_message(message.chat.id, "اختر تخصصاً من تخصصات الدبلوم الحضوري:", reply_markup=markup)

    elif text == "تخصصات برامج الدبلوم - عن بُعد":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("شرح - البلاك بورد / Blackboard")
        markup.row("دبلوم الإدارة المالية والمصرفية - عن بعد")
        markup.row("🔙 رجوع")
        bot.send_message(message.chat.id, "اختر من تخصصات الدبلوم عن بعد:", reply_markup=markup)

    elif text == "قناة وإعلانات الدبلوم 📢":
        reply = (
            "♦ قناة أخبار دبلومات جامعة الملك سعود:\nhttps://t.me/KSDN_222\n\n"
            "♦ قناة حلول واختبارات الدبلوم:\nhttps://t.me/Diploma_Solutions"
        )
        bot.send_message(message.chat.id, reply)

    elif text == "خدمات حل الواجبات وعمل المشاريع والبحوث":
        reply = (
            "🎓 منصة عونك الأكاديمية لطلاب الدبلوم:\n\n"
            "🔸 خدماتنا:\n"
            "▪️ حل واجبات\n▪️ إعداد بحوث\n▪️ تصميم عروض\n▪️ تنفيذ مشاريع\n▪️ دعم فصلي كامل\n\n"
            "📌 تابع القنوات:\nhttps://t.me/Diploma_Solutions\nhttps://t.me/Aoun_Academic\n\n"
            "💬 للتواصل عبر واتساب:\nhttps://wa.me/967733365187\n\n"
            "⭐ جودة، سرعة، خصوصية\n✍️ معكم حتى التخرج 🌿"
        )
        bot.send_message(message.chat.id, reply)

    elif text == "مواقع فروع جامعة الملك سعود":
        reply = (
            "📍 مواقع الفروع:\n\n"
            "• عليشة: https://maps.app.goo.gl/nHSKPBWHqAdvspmz8\n"
            "• الروابي: https://maps.app.goo.gl/1Xf9MqXCPs9fVkng7\n"
            "• تركي الأول: https://maps.app.goo.gl/NjeJTWoj4mhK5MUKA\n"
            "• الملز: https://maps.app.goo.gl/4bnaxNA8vMDRSp9D7\n"
            "• الوشم: https://maps.app.goo.gl/sCo9BkV1WaEeXVGa8\n"
            "• المدينة الجامعية: https://maps.app.goo.gl/EZcL9XVz1w8UomYF6"
        )
        bot.send_message(message.chat.id, reply)

    elif text == "شروط التجسير في جامعة الملك سعود":
        reply = "📌 شروط التجسير:\nhttps://t.me/Diploma_Solutions/24"
        bot.send_message(message.chat.id, reply)

    elif text == "🛑شرح استخدام – البلاك بورد / Blackboard 🛑":
        reply = "شرح البلاك بورد:\nhttps://t.me/Diploma_Solutions/16"
        bot.send_message(message.chat.id, reply)

    elif text == "🔙 رجوع":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(*left_commands)
        for tab in right_tabs:
            markup.add(tab)
        bot.send_message(message.chat.id, "تم الرجوع إلى القائمة الرئيسية.", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "عذراً، هذا القسم قيد التطوير أو غير معروف.")

# Webhook Handler
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route('/')
def webhook():
    # استبدل هذا الرابط برابط تطبيقك في Render
    bot.remove_webhook()
    bot.set_webhook(url='https://YOUR_RENDER_APP_URL/' + TOKEN)
    return "Webhook set", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    
