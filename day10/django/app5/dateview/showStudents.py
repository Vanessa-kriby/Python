from app1.models import *
from app1.util.utils import *

def showStudents(request):
    '''
        get:
            http://127.0.0.1:8000/app5/showStudents
    '''
    result=Student.objects.all().values("sno","sname","sgender","nation","native_place","studentDepartment__dno","studentDepartment__dname")
    return showJsonresult(result)
