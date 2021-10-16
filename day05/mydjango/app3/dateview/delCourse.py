from app1.models import *
from app1.util.utils import *


def delCourse(request):
    '''
    url:
        http://127.0.0.1:8000/app3/delCourse?couid=xxx
    调用参数：
        couid:课程编号
    '''
    try:
          if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            cou=data["couid"]
        # cou=request.GET.get("couid")
            result=Course.objects.filter(cno=cou).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)