from app1.models import *
from app1.util.utils import *

def displayTeachings(request):
    '''
    http://127.0.0.1:8000/app7/displayTeachings
    '''
    result=Teaching.objects.values()
    return showJsonresult(result)