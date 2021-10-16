from app1.models import *
from app1.util.utils import *

def getteachCourse(request):
    '''
    http://127.0.0.1:8000/app4/getteachCourse?tno=101
    '''
    tid=request.GET.get("tno")
    result=TeachPlan.objects.values("teacher__tno","teacher__tname","course__cname","department__dname").filter(teacher__tno=tid)
    return showJsonresult(result)