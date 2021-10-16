from django.http import HttpResponse,JsonResponse
from django.core import serializers
import json
import datetime

def showJsonresult(result):
    response={}
    try:
        response['msg']="good job!"
        response['err_num']=0
        response['data']=list(result)
        return HttpResponse(json.dumps(response,cls=CJsonEncoder),'application/json')
    except Exception as e:
        response['msg']=str(e)
        response['err_num']=1
        return HttpResponse(response)

def showJsonerror(response):
    return HttpResponse(json.dumps(response),'application/json')

class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            # 这里可以统一修改想要的格式
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            # 这里可以统一修改想要的格式
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)  