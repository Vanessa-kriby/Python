from app1.models import Grade
from app1.util.utils import *


def showGrades(request):
    '''
    http://127.0.0.1:8000/app1/showGrades
    '''
    result=Grade.objects.all().values()
    return showJsonresult(result)