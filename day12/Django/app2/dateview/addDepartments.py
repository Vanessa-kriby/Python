from app1.models import *
from app1.util.utils import *

'''
url:
    http://127.0.0.1:8000/app2/addDepartments?dno=xxx&dname=xxx
调用参数：
    dno:专业编号
    dname:专业名称
'''

def addDepartments(request):
   
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