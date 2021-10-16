from app1.models import *
from app1.util.utils import *

def getteachCourse(request):
    '''
    http://127.0.0.1:8000/app4/getteachCourse?tno=103
    '''
    tid=request.GET.get("tno")
    result=Inventory.objects.values("teachPlan__teacher__tno","teachPlan__teacher__tname","teachPlan__course__cname","teachPlan__department__dname","teachPlan__teach_date","teachPlan__credit","student__sname").filter(teachPlan__teacher__tno=tid)
    return showJsonresult(result)