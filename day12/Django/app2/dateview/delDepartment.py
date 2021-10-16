from app1.models import *
from app1.util.utils import *


def delDepartment(request):
    '''
    url：
    http://127.0.0.1:8000/app2/delDepartment?dno=xxx
    调用参数：
        dno:专业编号
    '''
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            dno=data["dno"]
        # dno=request.GET.get("dno")
            result=Department.objects.filter(dno=dno).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)