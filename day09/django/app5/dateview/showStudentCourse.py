from app1.models import *
from app1.util.utils import *

def showStudentCourse(request):
    '''
        http://127.0.0.1:8000/app5/showStudentCourse
    '''
    sid=request.GET.get("sno")
    result=Inventory.objects.filter(student__sno=sid).values("student__sno","student__sname","teacher__tname","teachPlan__course__cno","teachPlan__course__cname","teachPlan__credit","teachPlan__teach_date","teachPlan__evaluation_method")
    return showJsonresult(result)