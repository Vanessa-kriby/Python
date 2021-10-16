from app1.models import *
from app1.util.utils import *

def retriveStudent(request):
    '''
        get:
            http://127.0.0.1:8000/app5/retriveStudent?sno=001
        调用参数:
            sno:学号
    '''
    try:
        stuNum=request.GET.get('sno')
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