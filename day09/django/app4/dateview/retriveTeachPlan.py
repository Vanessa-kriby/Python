from app1.models import *
from app1.util.utils import *

def retriveTeachPlan(request):
    '''
    URL:
        http://127.0.0.1:8000/app4/retriveTeachPlan?tpno=001
        
    '''
    try:
        tpno=request.GET.get("tpno")
        result=TeachPlan.objects.values().get(tpno=tpno)
        response={}
        response['msg']='Success!'
        response['err_num']=0
        response['data']=result
        return JsonResponse(response,safe=False)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)