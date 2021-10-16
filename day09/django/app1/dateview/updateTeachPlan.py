from app1.models import *
from app1.util.utils import *

def updateTeachPlan(request):
    '''
    get:
        http://127.0.0.1:8000/app1/updateTeachPlan?tpno=001&credit=7.0&teach_date=2011-08-22&evaluation_method=考查
    post:
        http://127.0.0.1:8000/app1/updateTeachPlan
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for item in data:
        # tpid=request.GET.get("tpno")
        # cr=request.GET.get("credit")
        # te=request.GET.get("teach_date")
        # ev=request.GET.get("evaluation_method")

                tpid=item["tpno"]
                cr=item["credit"]
                te=item["teach_date"]
                ev=item["evaluation_method"]

                result=TeachPlan.objects.filter(tpno=tpid).update(credit=cr,teach_date=te,evaluation_method=ev)

        result=TeachPlan.objects.all().values("tpno","credit","teach_date","evaluation_method","department__dno","department__dname","course__cno","course__cname","teacher__tno","teacher__tname")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response) 