from app1.models import *
from app1.util.utils import *

def retriveTeacher(request):
    '''
    http://127.0.0.1:8000/app4/retriveTeacher?tno=101
    '''
    try:
        tid=request.GET.get("tno")
        result=Teacher.objects.values().get(tno=tid)
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