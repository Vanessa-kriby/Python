from app1.models import *
from app1.util.utils import *

def addCourses(request):
    '''
        get:
            http://127.0.0.1:8000/app2/addCourses?cno=001&cname=生物&textBook=武汉大学出版社出版&category=必修
        调用参数:
            cno:课程编号
            cname:课程名称
            textBook:教材
            category:课程类型
        post:
            http://127.0.0.1:8000/app2/addCourses
    '''
    try:
        if(request.method=='POST'):
            coudata=json.loads(request.body)
            data=coudata["data"]
            for item in data:
        # cid=request.GET.get("cno")
        # cna=request.GET.get("cname")
        # tbook=request.GET.get("textBook")
        # cate=request.GET.get("category")

                cid=item["cno"]
                cna=item["cname"]
                tbook=item["textBook"]
                cate=item["category"]

                result=Course()
                result.cno=cid
                result.cname=cna
                result.textBook=tbook
                result.category=cate
                result.save()

        result=Course.objects.all().values("cno","cname","textBook","category")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
