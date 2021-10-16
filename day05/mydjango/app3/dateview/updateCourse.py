from app1.models import *
from app1.util.utils import *


def updateCourse(request):
    '''
    url:
        http://127.0.0.1:8000/app3/updateCourse?couid=100&couname=xxx
    调用参数：
        couid:课程编号
        couname:课程名称
    '''

    try:
          if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            cou=data["couid"]
            Cname=data["couname"]
        # cou=request.GET.get("couid")
        # Cname=request.GET.get("couname")
            result=Course()
            result.cno=cou
            result.cname=Cname
            result.save()
            result=Course.objects.all().values()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)