from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{text}')
def get(message_request: MessageRequest):
    msg = TextSendMessage(text='Hello, Python!')
    msg1 = TextSendMessage(text='Hello, JavaScript!')
    txt = '$ LINE emoji $'
    emoji = [
        {
            "index": 0,
            "productId": "670e0cce840a8236ddd4ee4c",
            "emojiId": "001"
        },
        {
            "index": 13,
            "productId": "670e0cce840a8236ddd4ee4c",
            "emojiId": "002"
        }
    ]
    # print(txt.find('$', 2))

    emoji_message = TextSendMessage(text=txt, emojis=emoji)

    return [
        msg,
        msg1,
        emoji_message
    ]