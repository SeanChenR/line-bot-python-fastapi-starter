from typing import Text
from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import DatetimePickerAction
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{action_dt}')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='Menu',
            text='Please select',
            actions=[
                # mode: date, time, datetime
                DatetimePickerAction(label='請選擇日期', data='datetime_postback', mode='date')
            ]
        )
    )

    return [
        msg
    ]