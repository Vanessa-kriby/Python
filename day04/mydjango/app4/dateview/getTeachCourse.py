from app1.util.utils import * 
from app1.models import *


def getTeachCourse(request):   #成功
    '''
        http://127.0.0.1:8000/app4/getTeachCourse
    '''
    result=Teacher.objects.all().values('tno','tname','teachCourse__cname','teachCourse__cno')
    return showJsonresult(result)