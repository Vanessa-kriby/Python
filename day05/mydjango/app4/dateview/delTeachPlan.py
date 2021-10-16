from app1.util.utils import * 
from app1.models import *


def delTeachPlan(request):  #成功
    '''
        http://127.0.0.1:8000/app4/delTeachPlan?deid=x&couid=x
        调用参数:
            deid: 专业编号
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]

            did=data["deid"]
            cid=data["couid"]
            # did=request.GET.get("deid")
            # t1=TeachPlan.objects.get(department=did)

            result=TeachPlan.objects.filter(department=did).filter(course=cid).delete()
            
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)