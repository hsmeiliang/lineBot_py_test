import re

class MessageRouter():
    def __init__(self, routerType='text'):
        self._messageRouterMapping = {}
        self._routerType = routerType

    def findFuncRegex(self, message):
        for regPattern in self._messageRouterMapping:
            if re.match(regPattern, message):
                return self._messageRouterMapping[regPattern]
        return None

    def add(self, message, func):
        self._messageRouterMapping[message] = func
        print('1')

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