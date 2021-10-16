from app1.models import *
from app1.util.utils import *

def teachCourse(request):
    '''
        get:
            http://127.0.0.1:8000/app3/teachCourse?tno=001
        调用参数:
        tno:工号
    '''
    tid=request.GET.get("tno")
    result=Inventory.objects.filter(teachPlan__teacher__tno=tid).values("teachPlan__teacher__tname","teachPlan__course__cname","teachPlan__department__dname","teachPlan__teach_date","teachPlan__credit","student__sname")
    return showJsonresult(result)