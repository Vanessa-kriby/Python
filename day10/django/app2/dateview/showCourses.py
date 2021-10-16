from app1.models import *
from app1.util.utils import *

def showCourses(request):
    '''
        get:
            http://127.0.0.1:8000/app2/showCourses
    '''
    result=Course.objects.all().values("cno","cname","textBook","category")
    return showJsonresult(result)