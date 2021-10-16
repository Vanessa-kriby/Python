from app1.models import *
from app1.util.utils import *


def addCourses(request):
    '''
    url:
        http://127.0.0.1:8000/app3/addCourses?couid=100&couname=高等数学1
    调用参数：
        couid:课程编号
        couname:课程名称
    '''

    try:
          if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            for item in data:
                cou=item["couid"]
                Cname=item["couname"]
            # cou=request.GET.get("couid")
            # Cname=request.GET.get("couname")
                result=Course()
                result.cno=cou
                result.cname=Cname
                result.save()
            result=Course.objects.filter(cno=cou).values()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)