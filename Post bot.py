import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '8478752257:AAF8QnomULiQKAgbfiIkGdrcTY0p_ERWTKs'
# To'g'ri formatda guruh ID si
TARGET_CHATS = [
    -1003029763221,  # Sizning guruh ID si
    # Boshqa ID larni shu yerga qo'shing, masalan: -1009876543210
]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(
        "Assalomu alaykum! Menga matn yoki rasm yuboring, men uni belgilangan kanal va guruhlarga yuboraman."
    )

@dp.message(Command('getid'))
async def get_chat_id(message: Message):
    """Guruh/kanal ID sini olish uchun komanda"""
    await message.answer(f"Bu guruh/kanal ID si: {message.chat.id}")

@dp.message()
async def message_handler(message: Message):
    try:
        if message.chat.type != 'private':
            return  # Faqat shaxsiy chatdan qabul qilish

        # Foydalanuvchi ma'lumotlarini olish
        sender_name = message.from_user.full_name
        sender_id = message.from_user.id

        # Xabar pastidagi qo'shimcha ma'lumot
        sender_info = f"\n\nYuboruvchi: {sender_name} (ID: {sender_id})"

        success_count = 0
        for chat_id in TARGET_CHATS:
            logging.info(f"Xabar {chat_id} ga yuborilmoqda...")
            try:
                if message.photo:
                    # Rasm yuborilgan bo'lsa
                    photo = message.photo[-1].file_id
                    caption = (message.caption or "") + sender_info
                    await bot.send_photo(chat_id=chat_id, photo=photo, caption=caption)
                    logging.info(f"Rasm {chat_id} ga muvaffaqiyatli yuborildi.")
                elif message.text:
                    # Matn yuborilgan bo'lsa
                    text = message.text + sender_info
                    await bot.send_message(chat_id=chat_id, text=text)
                    logging.info(f"Matn {chat_id} ga muvaffaqiyatli yuborildi.")
                else:
                    await message.answer("Faqat matn yoki rasm yuborishingiz mumkin.")
                    return
                success_count += 1
            except Exception as chat_error:
                logging.error(f"{chat_id} ga yuborishda xatolik: {chat_error}")

        if success_count > 0:
            await message.answer(f"Xabaringiz {success_count} ta joyga muvaffaqiyatli yuborildi!")
        else:
            await message.answer("Hech qaysi joyga yuborilmadi. ID larni tekshiring.")

    except Exception as e:
        logging.error(f"Umumiy xatolik: {e}")
        await message.answer("Umumiy xatolik yuz berdi. Loglarni tekshiring.")

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Botni ishga tushirishda xatolik: {e}")
    finally:
        await bot.session.close()

if __name__ == '__main__':
    print("Bot ishga tushmoqda...")
    asyncio.run(main())