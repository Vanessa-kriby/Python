from app1.models import *
from app1.util.utils import *

def addTeachPlans(request):
    '''
    get:
        http://127.0.0.1:8000/app1/addTeachPlans?dno=002&cno=103&tno=103&tpno=004&credit=3.0&teach_date=2011-09-01&evaluation_method=考试
    post:
        http://127.0.0.1:8000/app1/addTeachPlans
    '''

    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for item in data:
        # did=request.GET.get("dno")
        # cid=request.GET.get("cno")
        # tid=request.GET.get("tno")
        # tpid=request.GET.get("tpno")
        # cr=request.GET.get("credit")
        # te=request.GET.get("teach_date")
        # ev=request.GET.get("evaluation_method")
 
                did=item["dno"]
                cid=item["cno"]
                tid=item["tno"]
                tpid=item["tpno"]
                cr=item["credit"]
                te=item["teach_date"]
                ev=item["evaluation_method"]
                
                Dno=Department.objects.get(dno=did)
                Cno=Course.objects.get(cno=cid)
                Tno=Teacher.objects.get(tno=tid)
                result=TeachPlan()
                result.department=Dno
                result.course=Cno
                result.teacher=Tno
                result.tpno=tpid
                result.credit=cr
                result.teach_date=te
                result.evaluation_method=ev
                result.save()

        result=TeachPlan.objects.all().values("tpno","credit","teach_date","evaluation_method","department__dno","department__dname","course__cno","course__cname","teacher__tno","teacher__tname")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)