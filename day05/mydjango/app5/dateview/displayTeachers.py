from app1.models import *
from app1.util.utils import *

def displayTeachers(request):
    '''
    URL:
        http://127.0.0.1:8000/app5/displayTeachers
    '''

    result=Teacher.objects.all().values()
    return showJsonresult(result)