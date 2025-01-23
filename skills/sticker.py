from typing import Text
from linebot.models import StickerSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{sticker}')
def get(message_request: MessageRequest):
    sticker = StickerSendMessage(package_id="6136", sticker_id="10551378")

    return [
        sticker
    ]