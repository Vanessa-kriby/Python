from app1.models import *
from app1.util.utils import *

def showAdvance(request):
    '''
        get:
            http://127.0.0.1:8000/app1/showAdvance
    '''
    
    result=Advance.objects.all().values("ano","week","teacher__tno","teacher__tname","classroom__crno","course__cno","course__cname")
    return showJsonresult(result)
    