from app1.models import *
from app1.util.utils import *

def retriveStudents(request):
    '''
    URL:
        http://127.0.0.1:8000/app5/retriveStudents?sno=2019001
    '''
    try:
        sno=request.GET.get("sno")
        result=Student.objects.values().get(sno=sno)
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
