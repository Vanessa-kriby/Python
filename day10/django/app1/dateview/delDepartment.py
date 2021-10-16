from app1.models import *
from app1.util.utils import *

def delDepartment(request):
    '''
        get:
            http://127.0.0.1:8000/app1/delDepartment?dno=001
        调用参数:
            dno:专业编号
        post:
            http://127.0.0.1:8000/app1/delDepartment
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
        # did=request.GET.get("dno")

            did=data["dno"]

            result=Department.objects.filter(dno=did).delete()

        result=Department.objects.all().values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)