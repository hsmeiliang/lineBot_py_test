#from linebot.models import PostbackAction, ButtonsTemplate, TemplateSendMessage, TextSendMessage
# from LineInitializer import line_bot_api, handler
# import constant
from linebot import (LineBotApi, WebhookHandler)
line_bot_api = LineBotApi('eeca7lo2Ebs14wFbm4AXhvU/5qj569ywDfMxQ9a4cZaIqDKE4TFiHNNWvUaah2A2clVoV9McprdK6K/guNEZiSV8P6+HRgPr2Z3mB+3it2r3q2IDUJByKbPMoGwTrduDjjXZiW5xAp2FWQzSC0Tc7wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3b99db8557a3bb97f24e626b0d84837c')

from linebot.models import *
#from LineInitializer import line_bot_api, handler
import requests
import datetime as dt
from datetime import datetime
import json
import threading
import time



class HealthReminder():
    def __init__(self, func_on = 0):
        self.func_on = func_on
    
    def turnOn(self):
        self.func_on = 1
    
    def turnOff(self):
        self.func_on = 0
    
    def healthMessage(self, event):

        def job1():
            line_bot_api.push_message('Ufbdbbd3db1cc8d560f45d5cd2519b290', TextSendMessage(text = 'push message'))
            
        def set_interval(func, sec):
            def func_wrapper():
                set_interval(func, sec)
                func()
            t = threading.Timer(sec, func_wrapper)
            t.start()
        return t

        timer = set_interval(job1, 60) # 5min
        # one day = 86400 sec
        if self.func_on == 0:
            if timer.is_alive():
                timer.cancel()
'''
class HealthGoalController():
    def __init__(self):
        pass
    
    @staticmethod
    def keepHealth(event):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = 'keep_health'))
        line_bot_api.push_message('Ufbdbbd3db1cc8d560f45d5cd2519b290', TextSendMessage(text = 'push message'))
    
    @staticmethod
    def loseWeight(event):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = 'lose_weight'))
'''