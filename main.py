import os
from flask import Flask, request
import telebot
from telebot import types

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("⚠️ متغير البيئة TELEGRAM_TOKEN غير موجود. الرجاء إضافته في إعدادات Render.")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# --- قوائم الردود ---

def start_message():
    return (
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

def left_side_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("star", "help")
    return markup

def right_side_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(
        "التبويب الاول: تقويم عام 1447ه‍",
        "التبويب الثاني: خدمات التواصل مع الجامعة",
        "التبويب الثالث: الاسئلة الشائعة_عام",
        "التبويب الرابع: تخصصات برامج الدبلوم - حضوري",
        "التبويب الخامس: تخصصات برامج الدبلوم - عن بُعد",
        "التبويب السادس: قناة وإعلانات الدبلوم 📢",
        "التبويب السابع: خدمات حل الواجبات وعمل المشاريع والبحوث",
        "التبويب الثامن: مواقع فروع جامعة الملك سعود",
        "التبويب التاسع: التجسير",
        "التبويب العاشر: 🛑شرح استخدام – البلاك بورد / Blackboard 🛑",
        "🔙 رجوع"
    )
    return markup

# --- معالج /start ---
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        start_message(),
        parse_mode="Markdown",
        reply_markup=left_side_keyboard()
    )
    bot.send_message(
        message.chat.id,
        "اختر التبويب من القائمة اليمنى:",
        reply_markup=right_side_keyboard()
    )

# --- معالج باقي الرسائل ---
@bot.message_handler(func=lambda m: True)
def all_messages(message):
    text = message.text.strip()

    # زرَي اليسار
    if text == "star":
        bot.send_message(
            message.chat.id,
            "اضغط على الأوامر الموجودة في القائمة (قائمة في يمين البوت) أدناه لتحصل على كل ما تحتاجه:\n\n"
            "🎯 نأمل أن تنال خدمتنا رضاكم وأن نكون عند حسن ظنكم…"
        )
        bot.send_message(message.chat.id, "اختر التبويب:", reply_markup=right_side_keyboard())
        return
    if text == "help":
        bot.send_message(message.chat.id, "فيديو #شــــــرح_استخدام_البوت سيتوفر قريبا")
        return

    # زر الرجوع
    if text == "🔙 رجوع":
        bot.send_message(message.chat.id, "تم الرجوع إلى القائمة الرئيسية ✅", reply_markup=right_side_keyboard())
        return

    # التبويبات (1–10)
    if text == "التبويب الاول: تقويم عام 1447ه‍":
        bot.send_message(message.chat.id, "التقويم الدراسي للعام الجامعي 1447هـ في جامعة الملك سعود لم يُنشر بشكل رسمي بعد")
        return

    if text == "التبويب الثاني: خدمات التواصل مع الجامعة":
        bot.send_message(message.chat.id,
            "عمادة السنه الاولى المشتركة\n"
            "SSHELP@CFY.KSU.EDU.SA\n"
            "00966-114694006\n\n"
            "الشؤون الطلابية\n"
            "ksugcc@ksu.edu.sa\n"
            "00966 1 8050141\n\n"
            "المشرف على وحدة التوجيه و الإرشاد الطلابي\n"
            "sg@cfy.ksu.edu.sa\n"
            "4694118\n"
            "رقم المكتب:  2484\n\n"
            "المشرف على وحدة شؤون الطلاب\n"
            "sa@cfy.ksu.edu.sa\n\n"
            "ايميلات عمادة القبول والتسجيل\n"
            "dar@ksu.edu.sa\n"
            "darweb@ksu.edu.sa\n\n"
            "ارقام عمادة القبول والتسجيل\n"
            "0114677722\n"
            "0118054402\n\n"
            "منسق الفيزياء\n"
            "nbennessib@ksu.edu.sa\n"
            "nalkathran@ksu.edu.sa\n\n"
            "منسق أحياء\n"
            "aalii@ksu.edu.sa\n"
            "somer@ksu.edu.sa\n\n"
            "منسق كيم\n"
            "amenizi@ksu.edu.sa\n"
            "zalmarhoon@ksu.edu.sa\n\n"
            "منسق/ة انجل\n"
            "mramadan@cfy.ksu.edu.sa\n"
            "h.alshareef@cfy.ksu.edu.sa\n\n"
            "فرع عليشة (بنات): 011 805 7331\n"
            "فرع الناصرية (الوشم): 0114036600"
        )
        return

    if text == "التبويب الثالث: الاسئلة الشائعة_عام":
        bot.send_message(message.chat.id,
            "●الاسئلة الشائعة -عام\n\n"
            "◇ حول القبول: https://dar.ksu.edu.sa/ar/FAQ\n"
            "◇ للمنتظمين: https://dar.ksu.edu.sa/ar/faqs\n"
            "◇ للخريجين: https://dar.ksu.edu.sa/ar/gfaq"
        )
        return

    if text == "التبويب الرابع: تخصصات برامج الدبلوم - حضوري":
        bot.send_message(message.chat.id,
            "- *دبلوم محاسبة*:\n"
            "🔹 **الدبلوم المتوسط في المحاسبة – جامعة الملك سعود**\n"
            "…\n🔙 رجوع",
            parse_mode="Markdown"
        )
        return

    if text == "التبويب الخامس: تخصصات برامج الدبلوم - عن بُعد":
        bot.send_message(message.chat.id,
            "• شرح - البلاك بورد: https://t.me/Diploma_Solutions/16\n"
            "• دبلوم الإدارة المالية والمصرفية – عن بعد\n…\n🔙 رجوع"
        )
        return

    if text == "التبويب السادس: قناة وإعلانات الدبلوم 📢":
        bot.send_message(message.chat.id,
            "♦ أخبار دبلومات جامعة الملك سعود: https://t.me/KSDN_222\n\n"
            "♦ قناة حلول الواجبات: https://t.me/Diploma_Solutions"
        )
        return

    if text == "التبويب السابع: خدمات حل الواجبات وعمل المشاريع والبحوث":
        bot.send_message(message.chat.id,
            "🎓 **منصة عونك الأكاديمية**\n"
            "…\n🔙 رجوع", parse_mode="Markdown"
        )
        return

    if text == "التبويب الثامن: مواقع فروع جامعة الملك سعود":
        bot.send_message(message.chat.id,
            "▫️ عليشة (بنات): https://maps.app.goo.gl/nHSKPBWHqAdvspmz8\n"
            "…\n🔙 رجوع"
        )
        return

    if text == "التبويب التاسع: التجسير":
        bot.send_message(message.chat.id, "شروط التجسير: https://t.me/Diploma_Solutions/24")
        return

    if text == "التبويب العاشر: 🛑شرح استخدام – البلاك بورد / Blackboard 🛑":
        bot.send_message(message.chat.id,
            "شرح البلاك بورد ⤵️\nhttps://t.me/Diploma_Solutions/16"
        )
        return

    # أي رسالة أخرى
    bot.send_message(message.chat.id, "❗ الأمر غير معروف، الرجاء استخدام القائمة.")

# --- Webhook Routes ---

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    return '', 200

@app.route('/', methods=['GET'])
def index():
    return "Bot is alive!", 200

if __name__ == '__main__':
    # إزالة webhook قديم وتعيين الجديد
    bot.remove_webhook()
    bot.set_webhook(url=f"https://comp102-bot-lbog.onrender.com/{TOKEN}")

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
