from telegram import Bot

from src.variables import token, start, welcome_buttons, welcome_img, get_code, completion_message, invalid, telegram_id_not_null
from src.keyboard_maker import make_keyboard
from src.request_handler import post_uid


class IranCIPBot(object):
    def __init__(self):
        self.bot = Bot(token=token)
        self.offset = 0
        self.buttons = make_keyboard(welcome_buttons)

    def loop(self):
        with open(welcome_img, 'r') as welcome_image:
            while True:
                updates = self.bot.get_updates(offset=self.offset, timeout=3)
                if updates:
                    for update in updates:
                        self.offset = update.update_id + 1
                        if update.message.text == start:
                            self.bot.send_photo(update.message.chat_id, welcome_image.buffer)
                            welcome_image.seek(0)
                        elif update.message.text == get_code:
                            telegram_uid = str(update.message.from_user.id)
                            telegram_name = update.message.from_user.username
                            if not telegram_name:
                                self.bot.send_message(update.message.chat_id, text=telegram_id_not_null)
                                continue
                            resp = post_uid(telegram_uid, telegram_name)
                            if resp['OK']:
                                discount_token = resp['token']
                                self.bot.send_message(update.message.chat_id, text=completion_message)
                                self.bot.send_message(update.message.chat_id, text=discount_token)
                            else:
                                self.bot.send_message(update.message.chat_id, text=resp['Error'])
                        else:
                            self.bot.send_message(update.message.chat_id, text=invalid)
