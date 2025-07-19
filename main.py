import telebot
from telebot import types

# بيانات البوت
TOKEN = '7684091983:AAHkXWM-jDaovpD4gWTngSkv-ahNNpIlgaI'
bot = telebot.TeleBot(TOKEN)

# لوحة الرئيسية
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("1️⃣ تخصصات برامج الدبلوم - حضوري", "2️⃣ تخصصات برامج الدبلوم - عن بعد")
    markup.row("3️⃣ قناة وإعلانات الدبلوم", "4️⃣ خدمات حل الواجبات والبحوث")
    markup.row("5️⃣ مواقع فروع جامعة الملك سعود", "6️⃣ التجسير", "7️⃣ شرح البلاك بورد")
    return markup

# قائمة حضوري
def حضوري_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("دبلوم محاسبة", "دبلوم التسويق", "دبلوم الأنظمة")
    markup.row("دبلوم البرمجة وقواعد البيانات", "دبلوم السكرتارية الطبية")
    markup.row("دبلوم الأعمال المصرفية", "دبلوم الوسائط المتعددة التفاعلية")
    markup.row("دبلوم الأمن السيبراني", "دبلوم السكرتارية التنفيذية")
    markup.row("دبلوم تقنية النظارات", "دبلوم إدارة الموارد البشرية")
    markup.row("دبلوم المحاسبة الضريبية", "دبلوم الترجمة بلغة الإشارة")
    markup.row("دبلوم مقدمي الرعاية بالحضانات", "دبلوم اللغة الصينية")
    markup.row("الدبلوم المشارك في العمل الخيري")
    markup.row("🔙 رجوع")
    return markup

# قائمة عن بعد
def عن_بعد_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("شرح - البلاك بورد / Blackboard")
    markup.row("دبلوم الإدارة المالية والمصرفية - عن بعد")
    markup.row("دبلوم إدارة أعمال التأمين - عن بعد")
    markup.row("دبلوم التسويق - عن بعد")
    markup.row("📚 كتب وملخصات مواد الدبلوم عن بعد PDF")
    markup.row("📌 خدمات طلابية ، متابعة الاعمال الفصليه")
    markup.row("🔙 BACK")
    return markup

# عند /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    text = (
        "◆ اضغط على الأوامر في القائمة في الأسفل وتطلع لك كل تفاصيل الدبلوم\n\n"
        "📣 قناة مساعدات طلاب الدبلوم:\n"
        "[اضغط هنا للدخول إلى القناة](https://t.me/Aoun_Academic)"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu())

# التعامل مع كل الرسائل الأخرى
@bot.message_handler(func=lambda m: True)
def menu_handler(message):
    text = message.text.strip()

    # رجوع للقائمة الرئيسية
    if text in ["🔙 رجوع", "🔙 BACK"]:
        bot.send_message(message.chat.id, "تم الرجوع إلى القائمة الرئيسية ✅", reply_markup=main_menu())

    elif text == "1️⃣ تخصصات برامج الدبلوم - حضوري":
        bot.send_message(message.chat.id, "اختر أحد تخصصات الدبلوم الحضوري:", reply_markup=حضوري_menu())

    elif text == "2️⃣ تخصصات برامج الدبلوم - عن بعد":
        bot.send_message(message.chat.id, "اختر أحد تخصصات الدبلوم عن بعد:", reply_markup=عن_بعد_menu())

    elif text == "3️⃣ قناة وإعلانات الدبلوم":
        bot.send_message(message.chat.id, "📢 قناة الإعلانات:\nhttps://t.me/KSDN_222")

    elif text == "4️⃣ خدمات حل الواجبات والبحوث":
        bot.send_message(message.chat.id, "📚 منصة عون الأكاديمية:\nhttps://wa.me/967733365187")

    elif text == "5️⃣ مواقع فروع جامعة الملك سعود":
        locations = (
            "▫️عليشة (بنات): https://maps.app.goo.gl/nHSKPBWHqAdvspmz8?g_st=it\n"
            "▫️الروابي (مشترك): https://maps.app.goo.gl/1Xf9MqXCPs9fVkng7?g_st=it\n"
            "▫️المبنى الرئيسي (تركي الأول): https://maps.app.goo.gl/NjeJTWoj4mhK5MUKA?g_st=it\n"
            "▫️الملز: https://maps.app.goo.gl/4bnaxNA8vMDRSp9D7\n"
            "▫️الوشم (عيال): https://maps.app.goo.gl/sCo9BkV1WaEeXVGa8?g_st=it\n"
            "▫️المدينة الجامعية للطالبات: https://maps.app.goo.gl/EZcL9XVz1w8UomYF6?g_st=ic"
        )
        bot.send_message(message.chat.id, locations)

    elif text == "6️⃣ التجسير":
        bridge = (
            "📌 شروط التجسير في جامعة الملك سعود:\n"
            "- معدل تراكمي بين 4.5 - 5\n"
            "- ألا يكون قد درس بكالوريوس سابقًا في الجامعة\n"
            "- مضى أقل من 5 سنوات على الحصول على الدبلوم\n"
            "- سعودي أو من أم سعودية\n"
            "- موافقة جهة العمل\n"
            "- استيفاء الشروط العامة"
        )
        bot.send_message(message.chat.id, bridge)

    elif text == "7️⃣ شرح البلاك بورد":
        bot.send_message(message.chat.id, "🎓 شرح البلاك بورد:\nالبلاك بورد هو نظام إدارة تعليم إلكتروني يستخدمه الطلاب للدخول إلى المحاضرات والمحتوى والاختبارات.\n(يمكنك طلب شرح مخصص لاحقًا).")

    else:
        bot.send_message(message.chat.id, "❗الأمر غير معروف، الرجاء استخدام القائمة.")

bot.infinity_polling()
