from linebot.models import *
import operator
import requests
import json
from datetime import datetime
import csv
import json


# Useless function
def TextAnalysis(text=''):
    disease = [1,0,1,0] # this line is temporarily added
    advise = '該菜單可能包含不宜多吃的食物:\n'
    abandon = []
    heart = ['炸', '牛', '豬', '羊', '薯條', '雞塊', '雞排', '酒', '辣', '香腸', '火腿'] # the keywords of abandoned food, except: '甜不辣', '牛角', '牛奶', '羊奶'
    diabete = ['米','飯','麵','麥','薯','地瓜','芋頭','薏仁','粥','吐司','可頌', # the keywords of abandoned food
             '餃','鍋貼','南瓜','冬粉','螞蟻上樹','饅頭','包','燒賣','油條', '堡', '派',
             '蔥油餅','蛋餅','貝果','三明治', '泡芙', '巧克力', '冰淇淋', '奶茶', '奶昔', '汽水', '可樂', '蘇打', '餅']
    bloodPressure = ['牛', '豬', '羊', '堡', '貢丸', '魚丸', '醬', '麵包', '餅乾', '蛋糕', '麵', '腰子', '雞皮', # the keywords of abandoned food, except: '甜不辣', '牛角', '牛奶', '羊奶'
             '鴨皮', '燻雞', '榨菜', '酸菜', '醬菜', '梅乾菜', '蜜餞', '肉鬆', '魚鬆', '火腿', '豆瓣', '辣椒', '沙茶',
             '豆腐乳', '肉醬', '奶油', '火鍋']
    belly = ['湯', '茶泡飯', '蕎麥', '醋', '生魚片', '生菜', '生雞蛋', '竹筍', '牛蒡', '南瓜', '芥菜', '蒟蒻', '海帶', '紫菜',
             '海苔', '藻', '柑', '橘', '椪', '橙', '草莓', '鳳梨', '檸', '檬', '番茄醬', '茄汁']

    for food in text.split('\n'):
        print(food)
        if disease[0] == 1: # diabete
            for f in diabete:
                if food.find(f) >= 0:
                    abandon.append(f)
                    break
        if disease[1] == 1: # heart
            for f in heart:
                if food.find(f) >= 0:
                    abandon.append(f)
                    break
        if disease[2] == 1: # blood pressure
            for f in bloodPressure:
                if food.find(f) >= 0:
                    abandon.append(f)
                    break
        if disease[3] == 1: # belly
            for f in belly:
                if food.find(f) >= 0:
                    abandon.append(f)
                    break

    abandon_set = set(abandon)
    if len(abandon_set) > 0: advise = advise + '\n'.join(list(abandon_set))
    return advise

def order(data):
    food = data.split(' ')
    answer = dict()
    veg = ['菜','番茄','茄子','茼蒿','冬瓜','苦瓜','青椒','沙拉','蘿蔔','菜頭',
           '筍','豆苗','豆芽','苜蓿','四季豆','豌豆']
    meat = ['肉','豬','蛋','雞','牛','羊','鴨','鵝','魚','蝦','貝',
            '透抽','小卷','中卷','小管','魷魚','章魚','蛤蜊','牡蠣',
            '黃豆','黑豆','豆漿','紅豆','綠豆','豆腐','豆皮','排骨',
            '肝連','火腿','培根','香腸','大腸','小腸']
    fat = ['牛奶','羊奶','奶油','黃油','牛油','豬油','橄欖油','麻油','葵花油',
           '花生','焗烤','開心果','杏仁','腰果','芝麻','扁桃仁','乳','胡桃',
           '核桃','榛果','栗','堅果','葵花籽','南瓜籽']
    grain = ['米','飯','麵','麥','薯','地瓜','芋頭','薏仁','粥','吐司','可頌',
             '餃','鍋貼','南瓜','冬粉','螞蟻上樹','饅頭','包','燒賣','油條',
             '蔥油餅','抓餅','蛋餅','貝果','三明治','堡', '派']
    fruit = ['莓','橘','柑','蘋','葡萄','蕉','龍眼','芭樂','木瓜','西瓜',
             '蓮霧','梨','李','桃子','柿','榴槤','石榴','荔枝','枸杞','萊姆',
             '檸','檬','橙','柚','文旦','杏子','水蜜桃','百香果','無花果',
             '火龍果']
    for f in food:
        tmp = f
        score = 0
        
        if f in veg: score = 5
        elif f in meat: score = 4
        elif f in fat: score = 3
        elif f in grain: score = 2
        elif f in fruit: score = 1
        else:
            for v in veg:
                if tmp.find(v) >= 0:
                    score = 5
                    tmp = tmp.replace(v, '')
                    break
            for fa in fat:
                if tmp.find(fa) >= 0:
                    if score > 0:
                        score = score - 0.5
                    else:
                        score = 3
                    tmp = tmp.replace(fa, '')
                    break
                
            for m in meat:
                if tmp.find('蛋糕') >= 0 or tmp.find('蛋捲') >= 0 or tmp.find('蛋塔') >= 0:
                    if score > 0:
                        score = score - 4
                    else:
                        score = -3
                    break
                if tmp.find(m) >= 0:
                    if score < 5 and score > 0:
                        score = score + 0.2
                    elif score == 5:
                        score = score - 0.5
                    else:
                        score = 4
                    tmp = tmp.replace(m, '')
                    break
            for g in grain:
                if score < 0:
                    break
                if tmp.find(g) >= 0:
                    if score > 0:
                        score = score - 2.5
                    else:
                        score = 2
                    tmp = tmp.replace(g, '')
                    break
            for fr in fruit:
                if score < 0:
                    break
                if tmp.find(fr) >= 0:
                    if score > 0:
                        score = score - 3.5
                    else:
                        score = 1
                    break
        
        if score == 0:
            score = -3
        
        print(f+' '+str(score))
        answer[f] = score
    return sorted(answer.items(), key=operator.itemgetter(1), reverse=True)

def foodConflict(foods):
    column = []
    with open('FoodConflictList.csv', 'r', encoding = "utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            column.append(row)
    # print(column)
    table = json.loads(json.dumps(column))
    conflictMsg = []
    suggestion = []
    for row in table:
        flag1 = 0
        flag2 = 0
        for food in foods:
            if row['food1'] == food:
                flag1 +=1
                break
            if row['food2'] == food:
                flag2 +=1
                break
            for i in range(len(food)):
                if row['food1'] == food[i]:
                    flag1 +=1
                    break
                elif row['food2'] == food[i]:
                    flag2 +=1
                    break
        if flag1 == 1 and flag2 == 1:
            conflictMsg.append(row)
        elif flag1 == 1 or flag2 == 1:
            suggestion.append(row)
    return conflictMsg, suggestion

def foodsMessage(conflictMsg):
    msg = ''
    num = 1
    for item in conflictMsg:
        msg = msg + str(num) +'. ' + '「' + item['food1'] + '」' + '和' + '「' + item['food2'] + '」' + '有食物衝突\n' + item['warning'] + '\n'
        num+=1
    return msg





