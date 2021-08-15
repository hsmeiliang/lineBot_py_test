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
                        TextComponent(text = "Dear " + user_name + " :", ),
                        TextComponent(text = warningmsg['content'], weight='bold', color='#cd5c5c'),
                        TextComponent(text = "Please checkout your body info.")
                    ]
                )
            ]
        )
    )
    message = FlexSendMessage(alt_text = 'Company Health Platform Message', contents = bubble) 
    line_bot_api.push_message(warningmsg['lineID'], message)

