from app1.util.utils import * 
from app1.models import *

def addTeachers(request):    #成功
    '''
        http://127.0.0.1:8000/app4/addTeachers?teid=x&teName=x&teGender=x&tejobTitle=x
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]

            tid=data["teid"]
            tName=data["teName"]
            tgender=data["teGender"]
            tjt=data["tejobTitle"]
            # tid=request.GET.get("teid")
            # tName=request.GET.get("teName")
            # tgender=request.GET.get("teGender")
            # tjt=request.GET.get("tejobTitle")
            result=Teacher()
            result.tno=tid
            result.tname=tName
            result.gender=tgender
            result.jobTitle=tjt
            result.save()
            result=Teacher.objects.values().filter(tno=tid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)