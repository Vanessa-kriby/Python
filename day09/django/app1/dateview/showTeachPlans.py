from app1.models import *
from app1.util.utils import *

def showTeachPlans(request):
    '''
        http://127.0.0.1:8000/app1/showTeachPlans
    '''
    result=TeachPlan.objects.all().values("tpno","credit","teach_date","evaluation_method","department__dno","department__dname","course__cno","course__cname","teacher__tno","teacher__tname")
    return showJsonresult(result)