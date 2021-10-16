from app1.models import *
from app1.util.utils import *

def delTeachPlan(request):
    '''
    get:
        http://127.0.0.1:8000/app1/delTeachPlan?tpno=002
    post:
        http://127.0.0.1:8000/app1/delTeachPlan
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
        # tpid=request.GET.get("tpno")

            tpid=data["tpno"]

            result=TeachPlan.objects.filter(tpno=tpid).delete()

        result=TeachPlan.objects.all().values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)