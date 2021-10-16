from app1.models import *
from app1.util.utils import *


def showCourses(request):
    '''
    http://127.0.0.1:8000/app4/showCourses
    '''

    try:
        result=Course.objects.all().values("cno","cname","textBook","category")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)