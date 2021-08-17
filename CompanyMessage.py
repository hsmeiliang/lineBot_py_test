import re
import requests
import json
from linebot.models import *
import string
# line_bot_api = LineBotApi('eeca7lo2Ebs14wFbm4AXhvU/5qj569ywDfMxQ9a4cZaIqDKE4TFiHNNWvUaah2A2clVoV9McprdK6K/guNEZiSV8P6+HRgPr2Z3mB+3it2r3q2IDUJByKbPMoGwTrduDjjXZiW5xAp2FWQzSC0Tc7wdB04t89/1O/w1cDnyilFU=')
# line_bot_api.push_message('Ufbdbbd3db1cc8d560f45d5cd2519b290', TextSendMessage(text = 'push message'))
# https://cdn4.iconfinder.com/data/icons/coronavirus-color/64/doctor-advise-warning-suggestion-avatar-1024.png
def PushMessage(line_bot_api):

    response = requests.post('https://virtserver.swaggerhub.com/v54dt/mhealth/1.0.0/notification')
    warningmsg = json.loads(response.text)
    print(warningmsg)
    warningmsg = json.loads(json.dumps({
        "lineID": "Ufbdbbd3db1cc8d560f45d5cd2519b290",
        "subject": "Health risk",
        "content": "Your health risk is low."
    }))
    
    user_name = 'xxx'
    msg = [TextComponent(text = "Dear " + user_name + " :"),
        TextComponent(text = warningmsg['content'], weight='bold', color='#cd5c5c')]
    if warningmsg['content'] == "Your health risk is high.":
        msg.append(TextComponent(text = "You should take good care of"))
        msg.append(TextComponent(text = "yourself and pay more attention to"))
        msg.append(TextComponent(text = "your health."))
    elif warningmsg['content'] == "Your health risk is medium.":
        msg.append(TextComponent(text = "You should take good care of"))
        msg.append(TextComponent(text = "yourself."))
    else:
        msg.append(TextComponent(text = "Keep going !"))
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
                    contents = msg
                )
            ]
        )
    )
    message = FlexSendMessage(alt_text = 'Company Health Platform Message', contents = bubble) 
    line_bot_api.push_message(warningmsg['lineID'], message)

def HealthRank(user_lineID, result):
    comp = []
    comp.append(TextComponent(text = "No." + "       " + "name" + "                  " + "value", color="#000000", flex=0))
    i = 0
    value = result["sortedData"]
    length = len(value)
    lineIDList = result["lineIDList"][0]
    for i in range(length):
        lineID = lineIDList[i]
        print(lineID, value[i])
        color = '#000000'

        user_name = "一二三"

        if lineID == user_lineID:
            color = '#4169E1'
        if i == 0:
            color = '#ffa500'
        
        space = "             "
        if value[i] < 0:
            space = "           "

        comp.append(TextComponent(text = str(i+1) + ".      " + user_name + space + str(value[i]), size = 'xl', color=color, flex=0))
        i+=1
    print(comp)
    
    for i in range(len(result["category"])):
        if result["category"][i].isupper():
            title = result["category"][:i] + ' ' + result["category"][i:] + ' '+ 'Rank'

    title = string.capwords(title)

    bubble = BubbleContainer(
        direction = 'ltr',
        body = BoxComponent(
            layout = 'vertical',
            contents = [BoxComponent(
                layout = 'vertical',
                contents = [
                    TextComponent(text=title, weight='bold', size='xl', color='#000000')
                ]
            ),
            BoxComponent(
                layout='vertical',spacing='md',margin='lg',
                contents=comp
            )
            ]
        )
    )
    return bubble
    
