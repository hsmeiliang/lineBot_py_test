import re
import requests
import json
from linebot.models import *
# line_bot_api = LineBotApi('eeca7lo2Ebs14wFbm4AXhvU/5qj569ywDfMxQ9a4cZaIqDKE4TFiHNNWvUaah2A2clVoV9McprdK6K/guNEZiSV8P6+HRgPr2Z3mB+3it2r3q2IDUJByKbPMoGwTrduDjjXZiW5xAp2FWQzSC0Tc7wdB04t89/1O/w1cDnyilFU=')
# line_bot_api.push_message('Ufbdbbd3db1cc8d560f45d5cd2519b290', TextSendMessage(text = 'push message'))
# https://cdn4.iconfinder.com/data/icons/coronavirus-color/64/doctor-advise-warning-suggestion-avatar-1024.png
def PushMessage(line_bot_api):
    '''
    response = requests.post('https://virtserver.swaggerhub.com/v54dt/mhealth/1.0.0/notification')
    warningmsg = json.loads(response.text)
    '''
    warningmsg = json.loads(json.dumps({
        "lineID": "Ufbdbbd3db1cc8d560f45d5cd2519b290",
        "subject": "Health risk",
        "content": "Your health risk is high."
    }))
    
    user_name = 'xxx'

    bubble = BubbleContainer(
        direction = 'ltr',
        body = BoxComponent(
            layout = 'vertical',
            contents = [
                BoxComponent(
                    layout = 'vertical',
                    contents = [
                        TextComponent(text = warningmsg['subject'], weight='bold', size='xl', color='#000000')
                    ]
                ),
                BoxComponent(
                    layout = 'vertical',
                    contents = [
                    ImageComponent(url = 'https://cdn4.iconfinder.com/data/icons/coronavirus-color/64/doctor-advise-warning-suggestion-avatar-1024.png')
                    ]
                ),
                BoxComponent(
                    layout = 'vertical',spacing='md',margin='xl',
                    contents = [
                        TextComponent(text = "Dear " + user_name + " :"),
                        TextComponent(text = warningmsg['content'], weight='bold', color='#cd5c5c'),
                        TextComponent(text = "Please checkout your body info.")
                    ]
                )
            ]
        )
    )
    message = FlexSendMessage(alt_text = 'Company Health Platform Message', contents = bubble) 
    line_bot_api.push_message(warningmsg['lineID'], message)

def HealthRank(user_lineID, result):
    comp = []
    i = 0
    value = result["sortedData"]
    lineIDList = result["lineIDList"]
    for lineID in lineIDList:
        print(lineID, value[i])
        color = '#696969'
        weight = 'normal'

        user_name = "xxx"

        if lineID == user_lineID:
            color = '#4169E1'
            weight = 'blod'
        if i == 1:
            color = '#ffa500'
            weight = 'blod'
        comp.append(
            BoxComponent(
                layout='horizontal',
                contents = [
                    TextComponent(text = str(i+1) + ".  ", weight=weight, color=color),
                    TextComponent(text = user_name, weight=weight, color=color),
                    TextComponent(text = str(value[i]), weight=weight, color=color)
                ]
            )
        )
        i+=1
        
    
    bubble = BubbleContainer(
        direction = 'ltr',
        body = BoxComponent(
            layout = 'vertical',
            contents = [
                BoxComponent(
                    layout = 'vertical',
                    contents = [
                        TextComponent(text = result["category"] + " Ranking", weight='bold', size='xl', color='#000000')
                    ]
                ),
                BoxComponent(
                    layout = 'vertical',spacing='md',margin='xl',
                    contents = [
                        TextComponent(text = "No.  "),
                        TextComponent(text = "name"),
                        TextComponent(text = "value", align='end'),
                        comp
                    ]
                )
            ]
        )
    )
    return bubble
    
