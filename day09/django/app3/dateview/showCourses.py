from app1.models import *
from app1.util.utils import *


def showCourses(request):
    '''
    http://127.0.0.1:8000/app3/showCourses
    '''

    try:
        result=Course.objects.all().values("cno","cname","textBook")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)