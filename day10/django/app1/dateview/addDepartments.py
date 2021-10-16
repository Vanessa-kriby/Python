from app1.models import *
from app1.util.utils import *

def addDepartments(request):
    '''
        get:
            http://127.0.0.1:8000/app1/addDepartments?dno=001&dname=2020计科
        调用参数:
            dno:专业编号
            dname:专业名称
        post:
            http://127.0.0.1:8000/app1/addDepartments
    '''
    try:
        if(request.method=='POST'):
            dpadata=json.loads(request.body)
            data=dpadata["data"]
            for item in data:
        # did=request.GET.get("dno")
        # dna=request.GET.get("dname")

                did=item["dno"]
                dna=item["dname"]              

                result=Department(dno=did,dname=dna)
                result.save()

        result=Department.objects.all().values("dno","dname")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)