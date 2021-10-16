from app1.models import *
from app1.util.utils import *

def retrieveTeacher(request):
    '''
        get:
            http://127.0.0.1:8000/app3/retrieveTeacher?tno=001
        调用参数:
            tno:工号
    '''
    try:
        teaNum=request.GET.get('tno')
        result=Teacher.objects.values().get(tno=teaNum)
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