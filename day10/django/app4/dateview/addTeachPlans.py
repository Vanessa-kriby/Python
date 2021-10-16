from app1.models import *
from app1.util.utils import *

def addTeachPlans(request):
    '''
        get:
            http://127.0.0.1:8000/app4/addTeachPlans?dno=001&cno=001&tno=001&tpno=001&credit=3.0&teach_date=2019-09-01&evaluation_method=考试
        调用参数:
            dno:专业编号
            cno:课程编号
            tno:工号
            tpno:计划编号
            credit:学分
            teach_date:开课日期
            evaluation_method:考察方式
        post:
            http://127.0.0.1:8000/app4/addTeachPlans
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