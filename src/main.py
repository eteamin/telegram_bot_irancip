from telegram import Bot

from variables import token, start, welcome_buttons, welcome_img, get_code, completion_message, invalid, telegram_id_not_null
from keyboard_maker import make_keyboard
from request_handler import post_uid


bot = Bot(token=token)
offset = 0
buttons = make_keyboard(welcome_buttons)
timeout = 3


def app():
    global offset
    with open(welcome_img, 'r') as welcome_image:
        while True:
            updates = bot.get_updates(offset=offset, timeout=timeout)
            if updates:
                for update in updates:
                    offset = update.update_id + 1
                    if update.message.text == start:
                        bot.send_photo(update.message.chat_id, welcome_image.buffer, reply_markup=buttons)
                        welcome_image.seek(0)
                    elif update.message.text == get_code:
                        telegram_uid = str(update.message.from_user.id)
                        telegram_name = update.message.from_user.username
                        if not telegram_name:
                            bot.send_message(update.message.chat_id, text=telegram_id_not_null)
                            continue
                        resp = post_uid(telegram_uid, telegram_name)
                        if resp['OK']:
                            discount_token = resp['token']
                            bot.send_message(update.message.chat_id, text=completion_message)
                            bot.send_message(update.message.chat_id, text=discount_token)
                        else:
                            bot.send_message(update.message.chat_id, text=resp['Error'])
                    else:
                        bot.send_message(update.message.chat_id, text=invalid)


app()
