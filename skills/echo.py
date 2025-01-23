from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{not_match}')
def get(message_request: MessageRequest):
    txt = 'Love Elulu $'
    emoji = [
        {
            "index": 11,
            "productId": "670e0cce840a8236ddd4ee4c",
            "emojiId": "001"
        },
    ]
    emoji_message = TextSendMessage(text=txt, emojis=emoji)
    return [
        TextSendMessage(text=f'You said : {message_request.message}'),
        emoji_message
    ]