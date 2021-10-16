from app1.models import *
from app1.util.utils import *

def updateCourse(request):
    '''
    url:
        http://127.0.0.1:8000/app3/updateCourse?cno=100&cname=xxx&textBook=xxx
    调用参数：
        couid:课程编号
        couname:课程名称
    '''

    try:
          if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            for item in data:
                cno=item["cno"]
                cname=item["cname"]
                textBook=item["textBook"]
            # cno=request.GET.get("cno")
            # cname=request.GET.get("cname")
            # textBook=request.GET.get("textBook")
                result=Course()
                result.cno=cno
                result.cname=cname
                result.textBook=textBook
                result.save()
            result=Course.objects.filter(cno=cno).values("cno","cname","textBook")
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)