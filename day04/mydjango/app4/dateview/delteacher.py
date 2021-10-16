
from app1.util.utils import * 
from app1.models import *


def delTeacher(request):  #成功
    '''
        http://127.0.0.1:8000/app4/delTeacher?teid=x
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]

            tid=data["teid"]
            # tid=request.GET.get("teid")
            t1=Teacher.objects.get(tno=tid)

            result=Teacher.objects.filter(tno=tid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)