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
import json
from BeaconMessage import BeaconMessage
beaconMessage = BeaconMessage()
from GetHealthEdu import GetYoutubeLink, GetNewsLink, HealthMessage
import CompanyMessage


#
# LINE 聊天機器人的基本資料
# LINE 的 channel_access_token, channel_secret 換成在 Line Developer 裡的資料

line_bot_api = LineBotApi('eeca7lo2Ebs14wFbm4AXhvU/5qj569ywDfMxQ9a4cZaIqDKE4TFiHNNWvUaah2A2clVoV9McprdK6K/guNEZiSV8P6+HRgPr2Z3mB+3it2r3q2IDUJByKbPMoGwTrduDjjXZiW5xAp2FWQzSC0Tc7wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3b99db8557a3bb97f24e626b0d84837c')
hwID_list = ['0125f93bd3', '0126846195']

app = Flask(__name__)
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

import schedule
import time
# 命名要小心 /keto, /ketoA   =>  /ketoA 讀不到
def job1():
    CompanyMessage.PushMessage(line_bot_api)
schedule.every(5).seconds.do(job1)

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
#####
####
####
###
status = 0

# 回傳 LINE 的資料
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    global status
    if text == 'advice':
        buttons_template = ButtonsTemplate(title='飲食建議',text='Eating suggestion',actions=[PostbackAction(label='生酮飲食',data='/ketogenicDiet'), PostbackAction(label='健身',data='/muscleDiet'),
                    PostbackAction(label='得舒飲食',data='/dashDiet'), PostbackAction(label='無麩質飲食',data='/glutenfreeDiet')])
        template_message = TemplateSendMessage(alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'video':
        getlinks = GetYoutubeLink()
        table=getlinks.getLinkLists()
        healthMessage=HealthMessage()
        message=healthMessage.showList(table)
        line_bot_api.reply_message(event.reply_token, message)
        ####
    elif text == 'news':
        getlinks = GetNewsLink()
        links, titles = getlinks.getLinkLists()
        healthMessage = HealthMessage()
        message = healthMessage.showNews(links, titles)
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'id':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(event.source.user_id))
    elif text == '排行榜':
        '''
        response = requests.post()
        result = json.loads(response.text)
        '''
        result = json.loads(json.dumps(
            {
                "category": "exerciseDuration",
                "lineIDList": [
                [
                    'Ufbdbbd3db1cc8d560f45d5cd2519b290',
                    'Ufbdbbd3db1cc8d560f45d5cd2519b291',
                    'Ufbdbbd3db1cc8d560f45d5cd2519b290',
                    'Ufbdbbd3db1cc8d560f45d5cd2519b291'
                ]
                ],
                "sortedData": [
                    40,
                    15,
                    13,
                    -34
                ]
            }
        ))
        message = FlexSendMessage(alt_text = 'health ranking', contents = CompanyMessage.HealthRank(event.source.user_id, result))
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'beacon':
        '''
        data = {
            'userID' : event.source.user_id,
            'kcal' : 10
        }
        response = requests.post(config.PHP_SERVER+'mhealth/Shop/RecommendShop.php', data = data)
        recommenList = json.loads(response.text)
        '''
        recommendList = json.loads(json.dumps([
            {'shopName' : '早餐店',
            'mealName' : '高熱量宅宅餐',
            'kcal' : 1200,
            'price' : 200,
            'picture' : 'https://i.imgur.com/376iFbj.jpg'
            },
            {'shopName' : '早餐店2',
            'mealName' : '高熱量宅宅餐2',
            'kcal' : 2200,
            'price' : 300,
            'picture' : 'https://i.imgur.com/376iFbj.jpg'
            }
        ]))
        message = [TextSendMessage(text= '附近餐點推薦'),
            FlexSendMessage(alt_text = '餐點推薦', contents = beaconMessage.nearbyFood(recommendList))]
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'enter hwid_list[0]':
        message = TextSendMessage(text = 'connect beacon 0 reply recommand food')
        line_bot_api.reply_message(event.reply_token, message)
    elif text == '路線':
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = '請輸入預定運動路線長度(km):\n範例:3'),
                                                    TextSendMessage(text = '若取消請輸入N')])
        status = 17
    elif text == '附近餐點推薦':
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = '請輸入最低熱量需求(kcal):\n範例:1000'),
                                                    TextSendMessage(text = '若取消請輸入N')])
        status = 18
    elif status == 17:
        if not isNum(text):
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='格式錯誤，請重新輸入'))
        else:
            '''
            data = {
                'userID' : event.source.user_id,
                'target_len' : text
            }
            response = requests.post(config.PHP_SERVER+'mhealth/SportPath/path.php', data = data)
            recommendPath = json.loads(response.text)
            '''
            recommendPath = json.loads(json.dumps(
                [{'start_position' : 123.123,
                'start_name' : '古亭河濱公園',
                'end_position' : 128.125,
                'end_name' : '馬場町紀念公園',
                'length' : 3900,
                'web' : 'https://reurl.cc/ZGEDn6'
                }]))
            message = FlexSendMessage(alt_text = '推薦路線', contents = beaconMessage.showPath(recommendPath))
            line_bot_api.reply_message(event.reply_token, message)
            status = 0
    elif status == 18:
        if not isNum(text):
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='格式錯誤，請重新輸入'))
        else:
            '''
            data = {
                'userID' : event.source.user_id,
                'kcal' : text
            }
            response = requests.post(config.PHP_SERVER+'mhealth/Shop/RecommendShop.php', data = data)
            recommenList = json.loads(response.text)
            '''
            recommendList = json.loads(json.dumps([
                {'shopName' : '早餐店',
                'mealName' : '高熱量宅宅餐',
                'kcal' : 1200,
                'price' : 200,
                'picture' : 'https://i.imgur.com/376iFbj.jpg'
                },
                {'shopName' : '早餐店2',
                'mealName' : '高熱量宅宅餐2',
                'kcal' : 2200,
                'price' : 300,
                'picture' : 'https://i.imgur.com/376iFbj.jpg'
                }
            ]))
            message = FlexSendMessage(alt_text = '餐點推薦', contents = beaconMessage.showList(recommendList))
            line_bot_api.reply_message(event.reply_token, message)
            status = 0

    
    


@handler.add(MessageEvent, message=ImageMessage)

@handler.add(PostbackEvent)
def handle_postback(event):
    if postbackRouter.route(event):
        return

@handler.add(BeaconEvent)
def handle_beacon(event):
    if event.beacon.hwid == "":
        message = TextSendMessage(text = 'success')
    else:
        message = TextSendMessage(text = 'not this position')
    if event.beacon.type == 'enter':
        data = {
            'updateInfo' : 'newBeacon',
            'userID' : event.source.user_id,
            'newBeacon' : event.beacon.hwid
        }
        response = requests.post(config.PHP_SERVER+'mhealth/lineUser/updateUserInfo.php', data = data)
        '''
        data = {
            'userID' : event.source.user_id,
            'kcal' : 10
        }
        response = requests.post(config.PHP_SERVER+'mhealth/Shop/RecommendShop.php', data = data)
        recommenList = json.loads(response.text)
        '''
        recommendList = json.loads(json.dumps([
            {'shopName' : '早餐店',
            'mealName' : '高熱量宅宅餐',
            'kcal' : 1200,
            'price' : 200,
            'picture' : 'https://i.imgur.com/376iFbj.jpg'
            },
            {'shopName' : '早餐店2',
            'mealName' : '高熱量宅宅餐2',
            'kcal' : 2200,
            'price' : 300,
            'picture' : 'https://i.imgur.com/376iFbj.jpg'
            }
        ]))
        message = [TextSendMessage(text= '附近餐點推薦'),
            FlexSendMessage(alt_text = '餐點推薦', contents = beaconMessage.nearbyFood(recommendList))]
    else:
        message = TextSendMessage(text = 'leave')
    line_bot_api.reply_message(event.reply_token, message)


def isNum(data):
    if len(data) > 1 and data[0] == '0': return False
    return data.replace('.', '', 1).isnumeric()


if __name__ == "__main__":
    while True :
        app.run()
        schedule.run_pending()
        time.sleep(10)
