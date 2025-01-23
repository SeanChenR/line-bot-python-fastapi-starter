from typing import Text
from linebot.models import TemplateSendMessage
from linebot.models.template import CarouselTemplate, CarouselColumn
from linebot.models.actions import MessageAction
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{carousel}')
def get(message_request: MessageRequest):
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://fakeimg.pl/300x300/?text=300x300',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        MessageAction(
                            label='Gfriend',
                            text='Gfriend'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://fakeimg.pl/300x300/?text=300x300',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        MessageAction(
                            label='ITZY',
                            text='ITZY'
                        ),
                    ]
                )
            ]
        )
    )

    return [
        carousel_template_message
    ]