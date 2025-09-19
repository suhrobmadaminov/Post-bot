Telegram Xabar Yuboruvchi Bot(Post bot)
Bu aiogram kutubxonasi yordamida Python’da yaratilgan Telegram boti. Bot foydalanuvchilardan shaxsiy chat orqali matn yoki rasm qabul qilib, ularni oldindan belgilangan Telegram guruh yoki kanallariga yuboradi. Bot asinxron operatsiyalarni boshqarish, faoliyatni log qilish va xatolarni samarali boshqarish uchun mo‘ljallangan.
Xususiyatlar

Komandalar:

/start: Botning funksiyasi haqida xush kelibsiz xabarini ko‘rsatadi.
/getid: Joriy chatning ID sini qaytaradi, bu guruh yoki kanallarni sozlash uchun foydali.


Xabar Yuborish:

Faqat shaxsiy chatlardan matn yoki rasm xabarlarini qabul qiladi.
Xabarlarni TARGET_CHATS ro‘yxatidagi guruh yoki kanallarga yuboradi.
Har bir yuborilgan xabarga yuboruvchining ismi va Telegram ID si qo‘shiladi.
Guruh yoki kanallardan kelgan xabarlarni e’tiborsiz qoldiradi, bu noto‘g‘ri yuborishning oldini oladi.


Xatolik Boshqaruvi va Loglash:

Python’ning logging moduli yordamida barcha operatsiyalar va xatolar loglanadi, bu nosozliklarni aniqlash va monitoring uchun qulay.
Foydalanuvchiga muvaffaqiyatli yuborilgan xabarlar soni yoki muvaffaqiyatsizlik haqida xabar beriladi.
Har bir chat va umumiy darajada xatolarni ushlab, boshqaradi.


Asinxron Ishlash:

asyncio va aiogram yordamida samarali, to‘xtovsiz xabar qayta ishlash.
Real vaqtda xabarlarni tinglash uchun polling rejimida ishlaydi.



Talablar

Python 3.7 yoki undan yuqori
aiogram kutubxonasi (pip install aiogram)

Kerakli kutubxonalarni o‘rnating:
bashpip install aiogram

Botni sozlang:

Kod ichidagi BOT_TOKEN ni Telegram Bot API tokeningiz bilan almashtiring (tokenni BotFather dan olishingiz mumkin).
TARGET_CHATS ro‘yxatini xabarlar yuboriladigan guruh yoki kanal ID lari bilan yangilang. Chat ID larini /getid komandasi orqali olishingiz mumkin.



Foydalanish

Botni ishga tushiring:
bashpython bot.py

Bot bilan ishlash:

Shaxsiy chatda /start yuboring va botning funksiyasi haqida ma’lumot oling.
Har qanday chatda /getid yuboring va chat ID sini oling.
Shaxsiy chatda matn yoki rasm yuboring, bot uni TARGET_CHATS ro‘yxatidagi barcha guruh/kanallarga yuboruvchi ma’lumotlari bilan birga yuboradi.



Kod Tuzilishi

Asosiy Komponentlar:

BOT_TOKEN: Telegram Bot API tokenini saqlaydi.
TARGET_CHATS: Xabarlar yuboriladigan guruh/kanal ID lari ro‘yxati.
start_handler: /start komandasini boshqaradi.
get_chat_id: /getid komandasi orqali chat ID sini qaytaradi.
message_handler: Kelgan matn yoki rasm xabarlarini qayta ishlaydi va yuboradi.
main: Botni ishga tushiradi va pollingni boshlaydi.


Loglash:

logging.basicConfig(level=logging.INFO) bilan sozlangan, barcha hodisalar va xatolar loglanadi.
Muvaffaqiyatli yuborishlar va xatoliklar haqida ma’lumot beradi.


Xatolik Boshqaruvi:

Xabar turi (matn/rasm) va chat turi (faqat shaxsiy) ni tekshiradi.
Har bir chat ID si uchun yuborishda xatoliklarni ushlaydi va loglaydi.
Foydalanuvchiga muvaffaqiyatli yuborilgan sonini bildiradi.



Qo‘shimcha Maslahatlar

Xavfsizlik: Bot tokenini va chat ID larini maxfiy saqlang. .env faylidan foydalanib, tokenni kod ichida yozmaslik tavsiya etiladi.
Kengaytirish: TARGET_CHATS ga ko‘proq ID qo‘shing yoki boshqa xabar turlarini (video, hujjat) qo‘llab-quvvatlash uchun kodni o‘zgartiring.
Muammolar: Agar bot ishlamasa, loglarni tekshiring yoki BOT_TOKEN va ID larni qayta tekshiring.
Litsenziya: Bu kod ochiq manbali, lekin foydalanishdan oldin litsenziyani ko‘rib chiqing.
