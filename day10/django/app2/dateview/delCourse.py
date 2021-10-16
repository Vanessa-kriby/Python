from app1.models import *
from app1.util.utils import *

def delCourse(request):
    '''
        get:
            http://127.0.0.1:8000/app2/delCourse?cno=001
        调用参数:
            cno:课程编号
        post:
            http://127.0.0.1:8000/app2/delCourse
    '''
    try:
        if(request.method=='POST'):
            coudata=json.loads(request.body)
            data=coudata["data"]
        # cid=request.GET.get("cno")
            
            cid=data["cno"]

            result=Course.objects.filter(cno=cid).delete()

        result=Course.objects.all().values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)