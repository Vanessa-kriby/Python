from app1.models import *
from app1.util.utils import *


def updateDepartment(request):
    '''
    url:
        http://127.0.0.1:8000/app2/updateDepartment?dno=01&dname=xxx
    调用参数:
        deid:专业编号
        dename:专业名称
    '''
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            for item in data:
                dno=item["dno"]
                dname=item["dname"]
            # dno=request.GET.get("dno")
            # dname=request.GET.get("dname")
                result=Department()
                result.dno=dno
                result.dname=dname
                result.save()
            result=Department.objects.filter(dno=dno).values("dno","dname")
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)