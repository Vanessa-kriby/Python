from app1.models import *
from app1.util.utils import *

def displayStudents(request):
    '''
    URL:
        http://127.0.0.1:8000/app6/displayStudents
    '''

    result=Student.objects.values("sno","sname","sgender","studentDepartment")
    return showJsonresult(result)