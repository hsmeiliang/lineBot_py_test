from linebot.models import PostbackAction, ButtonsTemplate, TemplateSendMessage, TextSendMessage
# from LineInitializer import line_bot_api, handler
# import constant
from linebot import (LineBotApi, WebhookHandler)
line_bot_api = LineBotApi('eeca7lo2Ebs14wFbm4AXhvU/5qj569ywDfMxQ9a4cZaIqDKE4TFiHNNWvUaah2A2clVoV9McprdK6K/guNEZiSV8P6+HRgPr2Z3mB+3it2r3q2IDUJByKbPMoGwTrduDjjXZiW5xAp2FWQzSC0Tc7wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3b99db8557a3bb97f24e626b0d84837c')

class HealthGoalController():
    def __init__(self):
        pass
    
    @staticmethod
    def keepHealth(event):
        line_bot_api.reply_message(event.reply_token, 'keep_health')
    
    @staticmethod
    def loseWeight(event):
        line_bot_api.reply_message(event.reply_token, 'lose_weight')