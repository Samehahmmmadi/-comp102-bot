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

    elif text == "الاسئلة الشائعة_عام":
        reply = (
            "● الأسئلة الشائعة - عام\n\n"
            "◇ الأسئلة الشائعة حول القبول:\n"
            "https://dar.ksu.edu.sa/ar/FAQ\n\n"
            "◇ الأسئلة الشائعة للطلاب المنتظمين:\n"
            "https://dar.ksu.edu.sa/ar/faqs\n\n"
            "◇ الأسئلة الشائعة للطلاب الخريجين:\n"
            "https://dar.ksu.edu.sa/ar/gfaq"
        )
        bot.send_message(message.chat.id, reply)

    elif text == "تخصصات برامج الدبلوم - حضوري":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("دبلوم محاسبة")
        markup.row("🔙 رجوع")
        bot.send_message(message.chat.id, "اختر تخصصاً من تخصصات الدبلوم الحضوري:", reply_markup=markup)

    elif text == "دبلوم محاسبة":
        reply = (
            "🔹 *الدبلوم المتوسط في المحاسبة – جامعة الملك سعود*\n"
            "**الرؤية العامة:**\n"
            "يهدف البرنامج إلى الإسهام في تلبية متطلبات سوق العمل السعودي من الكوادر المؤهلة في مجال المحاسبة، من خلال إعداد خريجين يمتلكون المعارف والمهارات اللازمة لأداء المهام المحاسبية بكفاءة واحترافية.\n\n"
            "### 🎯 *الأهداف الرئيسة للبرنامج:*\n"
            "✅ توفير بيئة أكاديمية متطورة لإعداد كوادر متميزة في المجال المحاسبي وفق منهج علمي دقيق.\n"
            "✅ تأهيل الطلبة بأحدث المفاهيم والمعارف النظرية والتطبيقية في المحاسبة.\n"
            "✅ تنمية المهارات الفكرية والبحثية للطلاب للعمل بكفاءة عالية في بيئات العمل المحاسبية.\n"
            "✅ تطوير المهارات العملية لإنجاز الأنشطة والعمليات المحاسبية المتنوعة.\n"
            "✅ تدريب الطلاب على استخدام الحاسب الآلي والتطبيقات المحاسبية الحديثة بكفاءة.\n"
            "✅ تقديم مرجعية علمية تجمع بين الجانب النظري والتطبيقي في مجال الأعمال المالية والمصرفية لخدمة الجامعات السعودية.\n\n"
            "---\n\n"
            "### 📚 *الخطة الدراسية ووصف المقررات:*\n\n"
            "* 🔸 [الخطة الدراسية للدبلوم المتوسط في المحاسبة (الجديدة)](https://ascs.ksu.edu.sa/sites/ascs.ksu.edu.sa/files/attach/%D8%A7%D9%84%D9%85%D8%AD%D8%A7%D8%B3%D8%A8%D8%A9_0.pdf)\n"
            "* 🔸 [وصف المقررات الدراسية للدبلوم المتوسط في المحاسبة (الجديدة)](https://ascs.ksu.edu.sa/sites/ascs.ksu.edu.sa/files/attach/wsf_lmqrrt_ldblwm_lmhsb.pdf)\n\n"
            "---\n\n"
            "### 💼 *الفرص الوظيفية للخريجين:*\n\n"
            "* مساعد محاسب\n"
            "* محصل إيرادات\n"
            "* مأمور مبيعات\n"
            "* أمين صندوق\n"
            "* مأمور عهد\n"
            "* مراقب عهد\n"
            "* مراقب مخازن\n"
            "* أمين مستودع\n"
            "* مفتش تموين\n"
            "* مأمور مشتريات\n"
            "* مراقب تجاري\n"
            "* مساعد مدقق حسابات\n"
            "* كاتب إداري في الإدارة المالية\n"
            "* مساعد مدرب في مجال التخصص\n\n"
            "https://t.me/SaudDiploma_bot"
        )
        bot.send_message(message.chat.id, reply, parse_mode="Markdown")

    elif text == "تخصصات برامج الدبلوم - عن بُعد":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("شرح - البلاك بورد / Blackboard")
        markup.row("دبلوم الإدارة المالية والمصرفية - عن بعد")
        markup.row("🔙 رجوع")
        bot.send_message(message.chat.id, "اختر من تخصصات الدبلوم عن بعد:", reply_markup=markup)

    elif text == "شرح - البلاك بورد / Blackboard":
        reply = "شرح استخدام- البلاك بورد/ Blackboard ⤵️\nhttps://t.me/Diploma_Solutions/16"
        bot.send_message(message.chat.id, reply)

    elif text == "دبلوم الإدارة المالية والمصرفية - عن بعد":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("تعريف بالتخصص")
        markup.row("الخطة الدراسية")
        markup.row("وصف المقررات")
        markup.row("🔙 رجوع")
        bot.send_message(message.chat.id, "اختر من قائمة دبلوم الإدارة المالية والمصرفية:", reply_markup=markup)

    elif text == "تعريف بالتخصص":
        reply = (
            "فيما يلي *ملخص منظم وشامل* لبرنامج *الدبلوم المتوسط في الإدارة المالية والمصرفية*:\n\n"
            "### 🎯 أهداف البرنامج:\n"
            "1. إكساب الطلاب المعرفة الأساسية بالمفاهيم والمبادئ والأنظمة في الإدارة المالية والمصرفية.\n"
            "2. تهيئة الطلاب للتطورات الحديثة في القطاع المالي والمصرفي.\n"
            "3. تأهيل الطلاب للعمل في الوظائف المالية والمصرفية المتنوعة.\n"
            "4. تنمية مهاراتهم العلمية والحسابية، إلى جانب مهارات التواصل وتقنية المعلومات.\n\n"
            "### 🎓 مخرجات تعلم البرنامج:\n"
            "**أولاً: المعرفة:**\n"
            "- التعرف على خصائص الأدوات المالية وأساليب التحليل المالي.\n"
            "- فهم أنواع المؤسسات والوسطاء الماليين وأدوارهم.\n"
            "- إدراك أساسيات الإدارة المالية والاستثمار.\n"
            "- متابعة التطورات والنظريات الحديثة في القطاع المالي والمصرفي.\n\n"
            "**ثانيًا: المهارات الإدراكية:**\n"
            "- استخدام البيانات المالية في التحليل وتقييم المشاريع.\n"
            "- تحليل القضايا المالية والتنبؤ بالمخاطر واتخاذ القرار.\n"
            "- التمييز بين الممارسات المالية المختلفة.\n"
            "- تقييم تغير المعلومات المالية بسرعة وفعالية.\n\n"
            "**ثالثًا: مهارات التعامل مع الأشخاص وتحمل المسؤولية:**\n"
            "- الوعي بالجوانب الأخلاقية المرتبطة بالمهنة.\n"
            "- التفاعل والعمل ضمن فرق العمل المتخصصة لتحقيق أهداف التخصص.\n\n"
            "**رابعًا: مهارات الاتصال، التقنية، والحساب:**\n"
            "- إتقان مهارات الاتصال الشفهي والكتابي باستخدام التقارير والعروض والبريد الإلكتروني.\n"
            "- توظيف التحليل الكمي والعددي في حل المشكلات.\n"
            "- استخدام الحاسب الآلي في المهام المالية والمصرفية.\n\n"
            "### 💼 الفرص الوظيفية:\n"
            "- المنشآت الاقتصادية بأنواعها\n"
            "- المصارف التجارية والإسلامية\n"
            "- شركات التأمين\n"
            "- البنك المركزي السعودي\n"
            "- مكاتب الصرافة\n"
            "- القطاعات المالية في الجهات الحكومية\n"
            "- وزارة المالية وأجهزتها المختلفة\n\n"
            "#### أمثلة للوظائف:\n"
            "- أمين صندوق\n"
            "- مأمور صرف\n"
            "- مساعد مدير مالي\n"
            "- مراقب مالي\n"
            "- عدّاد نقود\n"
            "- مدقق حسابات\n"
            "- محصّل إيرادات\n"
            "- مراقب تجاري\n"
            "- وغيرها من الوظائف ذات الصلة بالمجال المالي والمصرفي.\n\n"
            "https://t.me/SaudDiploma_bot"
        )
        bot.send_message(message.chat.id, reply, parse_mode="Markdown")

    elif text == "الخطة الدراسية":
        reply = "الخطة الدراسية للدبلوم المتوسط في الإدارة المالية والمصرفية:\nhttps://drive.google.com/file/d/11Re6r3MibiqyMxrlg0jh-X_SZGrOu5Cb/view?usp=drivesdk\n\nhttps://t.me/SaudDiploma_bot"
        bot.send_message(message.chat.id, reply)

    elif text == "وصف المقررات":
        reply = "وصف مقررات دبلوم الإدارة المالية والمصرفية:\nhttps://drive.google.com/file/d/11OtBZQauC278G2cqTkh2fSruXLHrqlf3/view?usp=drivesdk\n\nhttps://t.me/SaudDiploma_bot"
        bot.send_message(message.chat.id, reply)

    elif text == "🔙 رجوع":
        # أعيد عرض قائمة التبويبات الرئيسية في يمين البوت
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for tab in right_tabs:
            markup.add(tab)
        # أضف أوامر اليسار أيضاً
        markup.row(*left_commands)
        bot.send_message(message.chat.id, "تم الرجوع إلى القائمة الرئيسية.", reply_markup=markup)

    elif text == "قناة وإعلانات الدبلوم 📢":
        reply = (
            "♦ (قناة أخبار) دبلومات جامعة الملك سعود:\n"
            "🔗 https://t.me/KSDN_222\n\n"
            "♦ قناة خاصة بحلول واجبات واختبارات مواد الدبلوم بجامعة الملك سعود KSU:\n"
            "🔗 https://t.me/Diploma_Solutions"
        )
        bot.send_message(message.chat.id, reply)

    elif text == "خدمات حل الواجبات وعمل المشاريع والبحوث":
        reply = (
            "🎓 *منصة عونك الأكاديمية – لجميع طلاب دبلومات جامعة الملك سعود*\n\n"
            "🔸 سواء كنت طالبًا مستجدًا أو في أحد المستويات المتقدمة، وفرنا لك كل ما تحتاجه في مكانٍ واحد.\n\n"
            "💼 *خدماتنا تشمل:*\n"
            "▪️ حل الواجبات الأكاديمية بجودة عالية\n"
            "▪️ إعداد البحوث والتقارير الاحترافية (Word | PDF | Excel)\n"
            "▪️ تصميم العروض التقديمية PowerPoint بأسلوب مميز\n"
            "▪️ تنفيذ المشاريع الدراسية بدقة واحترافية\n"
            "▪️ دعم كامل في الأعمال الفصلية ومهام المواد\n\n"
            "🧠 نضم فريقًا من *المتخصصين الأكاديميين* في مختلف المجالات، نختار الأنسب لطلبك لضمان أعلى جودة ممكنة.\n\n"
            "📌 تابع قناتنا الرسمية لجميع الخدمات الطلابية:\n"
            "🔗 https://t.me/Diploma_Solutions\n"
            "🔗 https://t.me/Aoun_Academic\n\n"
            "💬 للتواصل وطلب الخدمات مباشرة:\n"
            "🔗 [اضغط هنا للتواصل عبر الواتساب](https://wa.me/967733365187)\n\n"
            "⭐️ *جودة، سرعة، خصوصية – لأن نجاحك هو هدفنا.*\n\n"
            "✍️ *معكم خطوة بخطوة حتى التخرج – دمتم بخير 🌿*"
        )
        bot.send_message(message.chat.id, reply, parse_mode="Markdown")

    elif text == "مواقع فروع جامعة الملك سعود":
        reply = (
            "⚪️ مواقع فروع جامعة الملك سعود:\n\n"
            "▫️ جامعة الملك سعود (عليشة بنات): https://maps.app.goo.gl/nHSKPBWHqAdvspmz8?g_st=it\n\n"
            "▫️ جامعة الملك سعود (الروابي مشترك): https://maps.app.goo.gl/1Xf9MqXCPs9fVkng7?g_st=it\n\n"
            "▫️ جامعة الملك سعود (المبنى الرئيسي تركي الأول): https://maps.app.goo.gl/NjeJTWoj4mhK5MUKA?g_st=it\n\n"
            "▫️ جامعة الملك سعود (الملز): https://maps.app.goo.gl/4bnaxNA8vMDRSp9D7\n\n"
            "▫️ جامعة الملك سعود (الوشم عيال): https://maps.app.goo.gl/sCo9BkV1WaEeXVGa8?g_st=it\n\n"
            "▫️ جامعة الملك سعود (المدينة الجامعية للطالبات): https://maps.app.goo.gl/EZcL9XVz1w8UomYF6?g_st=ic\n\n"
            "بوت الجامعة: https://t.me/SaudDiploma_bot"
        )
        bot.send_message(message.chat.id, reply)

    elif text == "شروط التجسير في جامعة الملك سعود":
        reply = "شروط التجسير في جامعة الملك سعود:\nhttps://t.me/Diploma_Solutions/24"
        bot.send_message(message.chat.id, reply)

    elif text == "🛑شرح استخدام – البلاك بورد / Blackboard 🛑":
        reply = "شرح استخدام- البلاك بورد/ Blackboard ⤵️\nhttps://t.me/Diploma_Solutions/16"
        bot.send_message(message.chat.id, reply)

    else:
        bot.send_message(message.chat.id, "عذراً، هذا القسم قيد التطوير أو غير معروف.")


# --- Webhook for Flask ---

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200


@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://YOUR_RENDER_APP_URL/' + TOKEN)
    return "Webhook set", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    
