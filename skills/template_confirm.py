from typing import Text
from linebot.models import TemplateSendMessage
from linebot.models.template import ConfirmTemplate
from linebot.models.actions import MessageAction
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{confirm}')
def get(message_request: MessageRequest):
    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='Are you sure?',
            actions=[
                MessageAction(
                    label='Yes',
                    text='YES'
                ),
                MessageAction(
                    label='No',
                    text='NO'
                )
            ]
        )
    )

    return [
        confirm_template_message
    ]