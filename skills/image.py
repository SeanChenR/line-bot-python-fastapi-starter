from typing import Text
from linebot.models import TextSendMessage, ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{image}')
def get(message_request: MessageRequest):
    msg = ImageSendMessage(
        original_content_url='https://fakeimg.pl/1024x768/?text=1024x768',
        preview_image_url='https://fakeimg.pl/800x600/?text=800x600')

    return [
        msg
    ]