from typing import Text
from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import LocationAction
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{action_location}')
def get(message_request: MessageRequest):

    location = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='Menu',
            text='地址選擇器',
            actions=[
                LocationAction(label='請選擇地址')
            ]
        )
    )

    return [
        location
    ]