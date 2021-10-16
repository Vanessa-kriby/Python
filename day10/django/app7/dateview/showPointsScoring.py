from app1.models import *
from app1.util.utils import *

def showPointsScoring(request):
    '''
        get:
            http://127.0.0.1:8000/app7/showPointsScoring
    '''
    result=PointsScoring.objects.all().values("inventory__ino""inventory__student","inventory__teachPlan__course__cname","score","credit","teacher__tname")
    return showJsonresult(result)