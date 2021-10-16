from app1.models import *
from app1.util.utils import *


def showDepartments(request):

    '''
     http://127.0.0.1:8000/app2/showDepartments
    '''
    try:
        result=Department.objects.all().values("dno","dname")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)