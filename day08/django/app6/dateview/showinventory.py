from app1.util.utils import * 
from app1.models import *


def showInventorys(request):   #成功
    '''
        http://127.0.0.1:8000/app6/showInventorys
    '''
    try:
        result=Inventory.objects.all().values('ino','teachPlan__department__dname','student__sno','student__sname','teachPlan__course__cname','teacher__tname','select_date')
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)