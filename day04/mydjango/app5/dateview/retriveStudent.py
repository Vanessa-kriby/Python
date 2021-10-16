from app1.models import *
from app1.util.utils import *

def retriveStudent(request):
    '''
        http://127.0.0.1:8000/app5/retriveStudent
    '''
    try:
        stuNum=request.GET.get('studentNum')
        result=Student.objects.values().get(sno=stuNum)
        response={}
        response['msg']='good job'
        response['err_num']=0
        response['data']=result
        return JsonResponse(response, safe=False)
        # return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)