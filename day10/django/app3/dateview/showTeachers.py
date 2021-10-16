from app1.models import *
from app1.util.utils import *

def showTeachers(request):
    '''
        get:
            http://127.0.0.1:8000/app3/showTeachers
    '''
    result=Teacher.objects.all().values("tno","tname","tgender","jobtitle")
    return showJsonresult(result)