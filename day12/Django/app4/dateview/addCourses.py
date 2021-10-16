from app1.models import *
from app1.util.utils import *


def addCourses(request):
    '''
    url:
        http://127.0.0.1:8000/app4/addCourses?cno=100&cname=xxx&textBook=xxx&category=xxx
    调用参数：
        cno:课程编号
        cname:课程名称
        textBook:教材
        category:类型
    '''

    try:
          if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            for item in data:
                cno=item["cno"]
                cname=item["cname"]
                textBook=item["textBook"]
                category=item["category"]
            # cno=request.GET.get("cno")
            # cname=request.GET.get("cname")
            # textBook=request.GET.get("textBook")
            # category=request.GET.get("category")
                result=Course()
                result.cno=cno
                result.cname=cname
                result.textBook=textBook
                result.category=category
                result.save()
            result=Course.objects.filter(cno=cno).values("cno","cname","textBook","category")
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)