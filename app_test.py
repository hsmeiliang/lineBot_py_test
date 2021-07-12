from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction, MessageTemplateAction,
    PostbackAction, DatetimePickerAction, URITemplateAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton, ImagemapSendMessage, BaseSize,
    URIImagemapAction, ImagemapArea, MessageImagemapAction
)

import BeaconMessage

app = Flask(__name__)
#
# LINE 聊天機器人的基本資料
# LINE 的 channel_access_token, channel_secret 換成在 Line Developer 裡的資料

line_bot_api = LineBotApi('eeca7lo2Ebs14wFbm4AXhvU/5qj569ywDfMxQ9a4cZaIqDKE4TFiHNNWvUaah2A2clVoV9McprdK6K/guNEZiSV8P6+HRgPr2Z3mB+3it2r3q2IDUJByKbPMoGwTrduDjjXZiW5xAp2FWQzSC0Tc7wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3b99db8557a3bb97f24e626b0d84837c')

from MessageRouter import MessageRouter
from controllers.EatIntroduceController import EatIntroduceController
postbackRouter = MessageRouter(routerType='postback')
postbackRouter.add('/ketogenicDiet', EatIntroduceController.ketogenicDiet)
postbackRouter.add('/ketoA', EatIntroduceController.ketoA)
postbackRouter.add('/ketoB', EatIntroduceController.ketoB)
postbackRouter.add('/ketoC', EatIntroduceController.ketoC)
postbackRouter.add('/muscleDiet', EatIntroduceController.muscleDiet)
postbackRouter.add('/muscleA', EatIntroduceController.muscleA)
postbackRouter.add('/muscleB', EatIntroduceController.muscleB)
postbackRouter.add('/muscleC', EatIntroduceController.muscleC)
postbackRouter.add('/dashDiet', EatIntroduceController.dashDiet)
postbackRouter.add('/dashA', EatIntroduceController.dashA)
postbackRouter.add('/dashB', EatIntroduceController.dashB)
postbackRouter.add('/dashC', EatIntroduceController.dashC)
postbackRouter.add('/glutenfreeDiet', EatIntroduceController.glutenfreeDiet)
postbackRouter.add('/glutenA', EatIntroduceController.glutenA)
postbackRouter.add('/glutenB', EatIntroduceController.glutenB)
postbackRouter.add('/glutenC', EatIntroduceController.glutenC)
print('done')
# 命名要小心 /keto, /ketoA   =>  /ketoA 讀不到

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    print(body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
#####
####
####
###

# 回傳 LINE 的資料
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    if text == 'advice':
        buttons_template = ButtonsTemplate(title='飲食建議',text='Eating suggestion',actions=[PostbackAction(label='生酮飲食',data='/ketogenicDiet'), PostbackAction(label='健身',data='/muscleDiet'),
                    PostbackAction(label='得舒飲食',data='/dashDiet'), PostbackAction(label='無麩質飲食',data='/glutenfreeDiet')])
        template_message = TemplateSendMessage(alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
def echo(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef": #因為LINE有些預設資料,我們在此排除
        try:

            #event.message.text = user傳的訊息
            '''
            # 回訊息
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="享社官網 : https://cruelshare.com/")
                # TextSendMessage(text=event.message.text) #鸚鵡說話
            )
            '''
            # 回圖片
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url="https://onepage.nownews.com/sites/default/files/2020-05/%E9%A6%96%E9%A0%81%E5%B0%81%E9%9D%A2-%E3%80%8C%E5%8F%AF%E6%86%90%E5%93%AA%E3%80%8D%E3%80%81%E3%80%8C%E9%BB%91%E4%BA%BA%E5%95%8F%E8%99%9F%E3%80%8D%E3%80%81%E3%80%8C%E6%88%91%E5%B0%B1%E7%88%9B%E3%80%8D%E9%80%99%E4%BA%9B%E6%A2%97%E5%9C%96%E7%9A%84%E7%94%B1%E4%BE%86%E4%BD%A0%E7%9F%A5%E9%81%93%E5%97%8E%EF%BC%9F.jpg",
                    preview_image_url="https://onepage.nownews.com/sites/default/files/2020-05/%E9%A6%96%E9%A0%81%E5%B0%81%E9%9D%A2-%E3%80%8C%E5%8F%AF%E6%86%90%E5%93%AA%E3%80%8D%E3%80%81%E3%80%8C%E9%BB%91%E4%BA%BA%E5%95%8F%E8%99%9F%E3%80%8D%E3%80%81%E3%80%8C%E6%88%91%E5%B0%B1%E7%88%9B%E3%80%8D%E9%80%99%E4%BA%9B%E6%A2%97%E5%9C%96%E7%9A%84%E7%94%B1%E4%BE%86%E4%BD%A0%E7%9F%A5%E9%81%93%E5%97%8E%EF%BC%9F.jpg"
                )
            )

            # 回影片
            VideoSendMessage(
              original_content_url='https://www.youtube.com/watch?v=NxOph87AtGc',
              preview_image_url='https://i.ytimg.com/vi/NxOph87AtGc/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAnNrD2Lewo_HJFJNEt1eejHd5U1w'
            )

            # 回地址
            LocationSendMessage(
              title='my location',
              address='Tokyo',
              latitude=35.65910807942215,
              longitude=139.70372892916203
            )

        except:

            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url="https://onepage.nownews.com/sites/default/files/2020-05/%E9%A6%96%E9%A0%81%E5%B0%81%E9%9D%A2-%E3%80%8C%E5%8F%AF%E6%86%90%E5%93%AA%E3%80%8D%E3%80%81%E3%80%8C%E9%BB%91%E4%BA%BA%E5%95%8F%E8%99%9F%E3%80%8D%E3%80%81%E3%80%8C%E6%88%91%E5%B0%B1%E7%88%9B%E3%80%8D%E9%80%99%E4%BA%9B%E6%A2%97%E5%9C%96%E7%9A%84%E7%94%B1%E4%BE%86%E4%BD%A0%E7%9F%A5%E9%81%93%E5%97%8E%EF%BC%9F.jpg",
                    preview_image_url="https://onepage.nownews.com/sites/default/files/2020-05/%E9%A6%96%E9%A0%81%E5%B0%81%E9%9D%A2-%E3%80%8C%E5%8F%AF%E6%86%90%E5%93%AA%E3%80%8D%E3%80%81%E3%80%8C%E9%BB%91%E4%BA%BA%E5%95%8F%E8%99%9F%E3%80%8D%E3%80%81%E3%80%8C%E6%88%91%E5%B0%B1%E7%88%9B%E3%80%8D%E9%80%99%E4%BA%9B%E6%A2%97%E5%9C%96%E7%9A%84%E7%94%B1%E4%BE%86%E4%BD%A0%E7%9F%A5%E9%81%93%E5%97%8E%EF%BC%9F.jpg"
                )
            )

@handler.add(PostbackEvent)
def handle_postback(event):
    if postbackRouter.route(event):
        return

@handler.add(BeaconEvent)
def handle_beacon(event):
    if event.beacon.hwid == "":
        message = 'success'
    else:
        message = 'fail'
    
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = message))


    


if __name__ == "__main__":
    app.run()