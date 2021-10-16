from app1.models import Student
from app1.util.utils import *

def showStudents(request):
    '''
        http://127.0.0.1:8000/app5/showStudents
    '''
    result=Student.objects.values().all()
    return showJsonresult(result)