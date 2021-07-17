from linebot.models import *

from linebot import (LineBotApi, WebhookHandler)
line_bot_api = LineBotApi('eeca7lo2Ebs14wFbm4AXhvU/5qj569ywDfMxQ9a4cZaIqDKE4TFiHNNWvUaah2A2clVoV9McprdK6K/guNEZiSV8P6+HRgPr2Z3mB+3it2r3q2IDUJByKbPMoGwTrduDjjXZiW5xAp2FWQzSC0Tc7wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3b99db8557a3bb97f24e626b0d84837c')
import json



class BeaconMessage():
    def __init__(self):
        pass

    def buildComponent(self):
        return BubbleContainer(
            direction = 'ltr',
            body = BoxComponent(
                layout = 'vertical',
                contents = [BoxComponent(
                    layout = 'vertical',
                    contents = [
                        TextComponent(text='附近飲食推薦', weight='bold', size='xl'),
                        TextComponent(text='以下是為你推薦附近的午餐菜單', weight='bold', size='xs', color='#555555'),
                        TextComponent(text='點擊即可新增飲食紀錄', weight='bold', size='xs', color='#555555')
                    ]
                ),
                BoxComponent(
                    layout='vertical',spacing='xs',margin='xl',
                    contents=[
                        BoxComponent(
                            layout='horizontal',
                            contents=[
                                TextComponent(text='皿富器食 minfood 花雕野菜', weight='bold', size='md', color='#555555', flex=0),
                                TextComponent(text='$' + str(255), weight='bold', size='md', color='#111111', align='end')
                            ]
                        ),
                        TextComponent(text='餐點熱量為' + str(340) + '大卡', weight='bold', size='xs', color='#555555'),
                        ImageComponent(url='https://i.imgur.com/376iFbj.jpg', margin='none',align='center',size='4xl')
                    ]
                )
                ]
            )
        )

    def showPath(self, recommendPath):
        comp = []
        for item in recommendPath:
            comp.append(
                BoxComponent(
                    layout='horizontal',
                    contents=[
                        TextComponent(text=item['start_name'], weight='bold', size='lg', color='#111111', flex=0),
                        TextComponent(text=' ' + '往'+' ', weight='bold', size='md', color='#555555', flex=0)
                    ]
                )
            )
            comp.append(TextComponent(text=item['end_name'], weight='bold', size='lg', color='#111111', flex=0, align='end'))
            '''
            comp.append(
                BoxComponent(
                    layout='horizontal',
                    contents=[
                        TextComponent(text=str(item['start_position']), weight='bold', size='md', color='#555555'),
                        TextComponent(text=str(item['end_position']), weight='bold', size='md', color='#555555', align='end')
                    ]
                )
            )
            '''
            comp.append(TextComponent(text='路線總長:'+str(item['length'])+'km', weight='bold', size='md', color="#a52a2a", align='end'))
            

        bubble = BubbleContainer(
            direction = 'ltr',
            body = BoxComponent(
                layout = 'vertical',
                contents = [BoxComponent(
                    layout = 'vertical',
                    contents = [
                        TextComponent(text='推薦路線', weight='bold', size='xl', color='#696969')
                    ]
                ),
                BoxComponent(
                    layout='vertical',spacing='md',margin='xl',
                    contents=comp
                ),
                ButtonComponent(
                    action=URIAction(label="開啟google看詳細資訊", uri=item['web']),
                    style='secondary', color="#87cefa"
                )
                ]
            )
        )
        return bubble



    def showList(self, recommendList):
        comp = []
        for item in recommendList:
            comp.append(TextComponent(text=item['shopName'], weight='bold', size='lg', color='#000000', flex=0))
            comp.append(
                BoxComponent(
                    layout='horizontal',
                    contents=[
                        TextComponent(text=' ' + '推薦'+' ', weight='bold', size='xs', color='#ffa500', flex=0),
                        TextComponent(text=item['mealName'], weight='bold', size='lg', color='#2f4f4f', flex=0),
                        TextComponent(text='$' + str(item['price']), weight='bold', size='md', color='#111111', align='end')
                    ]
                )
            )
            comp.append(
                BoxComponent(
                    layout='horizontal',
                    contents=[
                        TextComponent(text='餐點熱量為 ', weight='bold', size='xs', color='#111111', flex=0),
                        TextComponent(text=str(item['kcal']) + '大卡', weight='bold', size='md', color='#cd5c5c', flex=0)
                    ]
                )
            )
            # comp.append(TextComponent(text='餐點熱量為' + str(item['kcal']) + '大卡', weight='bold', size='xs', color='#555555'))
            comp.append(ImageComponent(url=item['picture'], margin='none',align='center',size='4xl'))
            comp.append(TextComponent(text=' ', size='md'))

        bubble = BubbleContainer(
            direction = 'ltr',
            body = BoxComponent(
                layout = 'vertical',
                contents = [BoxComponent(
                    layout = 'vertical',
                    contents = [
                        TextComponent(text='附近飲食推薦', weight='bold', size='xl', color='#696969')
                    ]
                ),
                BoxComponent(
                    layout='vertical',spacing='md',margin='xl',
                    contents=comp
                )
                ]
            )
        )
        return bubble
    @staticmethod
    def noThanks(event):
        pass
    @staticmethod
    def nearbyFood(event):
        '''
        kcal = event.postback.data
        data = {
            'userID' : event.source.user_id,
            'kcal' : kcal
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
        # beaconMessage = BeaconMessage()
        message = FlexSendMessage(alt_text = '餐點推薦', contents = showList(recommendList))
        line_bot_api.reply_message(event.reply_token, message)

