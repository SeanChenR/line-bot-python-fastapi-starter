from typing import Text
from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import MessageAction
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{buttons}')
def get(message_request: MessageRequest):
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://fakeimg.pl/300x300/?text=300x300',
            title='Menu',
            text='Please select',
            actions=[
                    MessageAction(
                            label='message',
                            text='message text'
                    ),
            ]
        )
    )

    return [
        buttons_template_message
    ]