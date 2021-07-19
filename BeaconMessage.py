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

    def nearbyFood(self, recommendList):
        return FlexSendMessage(alt_text= '餐點推薦', contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": true
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "東京旅行",
                    "wrap": true,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip11.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brow&Cony's Restaurant",
            "weight": "bold",
            "size": "sm",
            "wrap": true
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "東京旅行",
                    "wrap": true,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip12.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Tata",
            "weight": "bold",
            "size": "sm"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "東京旅行",
                    "wrap": true,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
}
        )
        

