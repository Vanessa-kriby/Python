from app1.models import *  
from app1.util.utils import *

def addTeachPlans(request):
    '''
        http://127.0.0.1:8000/app4/addTeachPlans?couid=100&deid=05&cre=5&tdate=2019-8-18&method=考试
        调用参数:
            couid: 课程编号
            deid: 专业编号
            cre:  学分
            tdate: 开课时间
            method: 考核方式
    '''
    try:
        if (request.method == 'POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for item in data:
                cid=item["couid"]
                did=item["deid"]
                cred=item["cre"]
                time=item["tdate"]
                met=item["method"]

                # cid=request.GET.get("couid")
                # did=request.GET.get("deid")
                # cred=request.GET.get("cre")
                # time=request.GET.get("tdate")
                # met=request.GET.get("method")
        
                coid=Course.objects.get(cno=cid)
                dmid=Department.objects.get(dno=did)
                result=TeachPlan()
                result.course=coid
                result.department=dmid
                result.credit=cred
                result.teach_date=time
                result.evaluation_method=met
                result.save()
                result=TeachPlan.objects.values().filter(department=did)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)