from app1.models import *
from app1.util.utils import *

def displayConsequences(request):
    '''
    url:
        http://127.0.0.1:8000/app1/displayConsequences
    '''
    result=Consequence.objects.values().all()
    return showJsonresult(result)