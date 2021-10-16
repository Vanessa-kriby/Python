from app1.models import *
from app1.util.utils import *

def showStudents(request):
    '''
    http://127.0.0.1:8000/app5/showStudents
    '''
    result=Student.objects.all().values("sno","sname","sgender","studentDepartment__dname")
    return showJsonresult(result)