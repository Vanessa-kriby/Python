from app1.models import Course
from app1.util.utils import *

def showCourses(request):
    '''
    http://127.0.0.1:8000/app2/showCourses
    '''
    result=Course.objects.all().values("cname","cno","textBook")
    return showJsonresult(result)
