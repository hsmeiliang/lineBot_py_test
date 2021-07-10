import re

class MessageRouter():
    def __init__(self, routerType='text'):
        self._messageRouterMapping = {}
        self._routerType = routerType

    @staticmethod
    def findFuncRegex(self, message):
        for regPattern in self._messageRouterMapping:
            if re.match(regPattern, message):
                return self._messageRouterMapping[regPattern]
        return None

    @staticmethod
    def add(self, message, func):
        self._messageRouterMapping[message] = func

    @staticmethod
    def route(self, event):
        if (self._routerType == 'text'):
            func = self.findFuncRegex(event.message.text)
            print('text')
        elif (self._routerType == 'postback'):
            func = self.findFuncRegex(event.postback.data)
            print('postback')
        if (func != None):
            func(event)
            print('action')
        else:
            print('None')
        return func != None