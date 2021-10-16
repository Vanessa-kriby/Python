from app1.models import *
from app1.util.utils import *

def showStudentCourse(request):
    '''
        get:
            http://127.0.0.1:8000/app5/showStudentCourse?sno=001
        调用参数:
            sno:学号
    '''
    sid=request.GET.get("sno")
    result=Inventory.objects.filter(student__sno=sid).values("ino","teachPlan__course__cname","teachPlan__teacher__tname","teachPlan__teach_date","teachPlan__credit","teachPlan__evaluation_method")
    return showJsonresult(result)