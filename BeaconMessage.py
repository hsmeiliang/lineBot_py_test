from linebot.models import *

from linebot import (LineBotApi, WebhookHandler)
line_bot_api = LineBotApi('eeca7lo2Ebs14wFbm4AXhvU/5qj569ywDfMxQ9a4cZaIqDKE4TFiHNNWvUaah2A2clVoV9McprdK6K/guNEZiSV8P6+HRgPr2Z3mB+3it2r3q2IDUJByKbPMoGwTrduDjjXZiW5xAp2FWQzSC0Tc7wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3b99db8557a3bb97f24e626b0d84837c')



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

    def showPath(recommendPath):
        pass


    def showList(self, recommendList):
        comp = []
        for item in recommendList:
            comp.append(
                BoxComponent(
                    layout='horizontal',
                    contents=[
                        TextComponent(text=item['shopName'], weight='bold', size='md', color='#555555', flex=0),
                        TextComponent(text='推薦', weight='bold', size='xs', color='#555555', flex=0),
                        TextComponent(text=item['mealName'], weight='bold', size='md', color='#555555', flex=0),
                        TextComponent(text='$' + str(item['price']), weight='bold', size='md', color='#111111', align='end'),
                    ]
                )
            )
            comp.append(TextComponent(text='餐點熱量為' + str(item['kcal']) + '大卡', weight='bold', size='xs', color='#555555'))
            comp.append(ImageComponent(url=item['picture'], margin='none',align='center',size='4xl'))

        bubble = BubbleContainer(
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
                    contents=comp
                )
                ]
            )
        )
        return bubble

