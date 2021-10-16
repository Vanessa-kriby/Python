from app1.util.utils import * 
from app1.models import *


def showTeachers(request):   #成功
    '''
        http://127.0.0.1:8000/app4/showTeachers
    '''
    result=Teacher.objects.all().values()
    return showJsonresult(result)