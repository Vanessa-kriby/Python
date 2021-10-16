from app1.models import *
from app1.util.utils import *

def showDepartments(request):
    '''
        get:
            http://127.0.0.1:8000/app1/showDepartments
    '''
    result=Department.objects.all().values("dno","dname")
    return showJsonresult(result)