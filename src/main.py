from telegram import Bot

from src.variables import token, start, welcome_buttons, welcome_text, register, completion_message
from src.keyboard_maker import make_keyboard
from src.request_handler import post_uid


class IranCIPBot(object):
    def __init__(self):
        self.bot = Bot(token=token)
        self.offset = 0
        self.buttons = make_keyboard(welcome_buttons)

    def loop(self):
        while True:
            updates = self.bot.get_updates(offset=self.offset, timeout=3)
            if updates:
                for update in updates:
                    self.offset = update.update_id + 1
                    if update.message.text == start:
                        self.bot.send_message(update.message.chat_id, text=welcome_text, reply_markup=self.buttons)
                    elif update.message.text == register:
                        telegram_uid = str(update.message.from_user.id)
                        discount_token = post_uid(telegram_uid)
                        self.bot.send_message(update.message.chat_id, text=completion_message)
                        self.bot.send_message(update.message.chat_id, text=discount_token)
