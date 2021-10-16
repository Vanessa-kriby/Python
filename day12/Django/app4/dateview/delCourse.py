from app1.models import *
from app1.util.utils import *


def delCourse(request):
    '''
    url:
        http://127.0.0.1:8000/app4/delCourse?cno=xxx
    调用参数：
        cno:课程编号
    '''
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            cno=data["cno"]
        # cno=request.GET.get("cno")
            result=Course.objects.filter(cno=cno).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)