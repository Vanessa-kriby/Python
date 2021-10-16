from app1.util.utils import * 
from app1.models import *

def updateTeacher(request):   #完成
    '''
        http://127.0.0.1:8000/app4/updateTeacher?teid=x&teName=x&teGender=x&tejobTitle=x
    '''
    try:
        tid=request.GET.get("teid")
        tName=request.GET.get("teName")
        tgender=request.GET.get("teGender")
        tjt=request.GET.get("tejobTitle")
        result=Teacher.objects.get(tno=tid) #根据条件找出符合的数据
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