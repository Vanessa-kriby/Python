from app1.models import *
from app1.util.utils import *

def showInventorys(request):
    '''
        get:
            http://127.0.0.1:8000/app6/showInventorys
    '''
    result=Inventory.objects.all().values("ino","select_date","teachPlan__tpno","student__sno","student__sname","teachPlan__course__cname","teachPlan__course__cno","teachPlan__department__dno","teachPlan__department__dname")
    return showJsonresult(result)