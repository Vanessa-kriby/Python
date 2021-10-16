from app1.util.utils import * 
from app1.models import *

def updateTeachPlan(request):   #完成
    '''
        http://127.0.0.1:8000/app4/updateTeachPlan?couid=100&deid=05&newcouid=04&cre=6&tdate=2019-8-19&method=不考试
        调用参数:
            couid: 课程编号
            newcouid: 更改的课程编号
            deid: 专业编号
            cre:  学分
            tdate: 开课时间
            method: 考核方式
        说明: 只允许修改专业中的课程
    '''
    try:
        # if (request.method == 'POST'):
        #     teadata=json.loads(request.body)
        #     data=teadata["data"]
            # for item in data:
            #     cid=item["couid"]
            #     did=item["deid"]
            #     cred=item["cre"]
            #     time=item["tdate"]
            #     met=item["method"]
        newcid=request.GET.get("newcouid")
        cid=request.GET.get("couid")
        did=request.GET.get("deid")
        cred=request.GET.get("cre")
        time=request.GET.get("tdate")
        met=request.GET.get("method")

        jia1=Department.objects.get(dno=did)
        jia2=Course.objects.get(cno=newcid)
        shan=TeachPlan.objects.filter(department=did).filter(course=cid).delete() #找到之后删除

        result=TeachPlan()
        result.course=jia2
        result.department=jia1
        result.credit=cred
        result.teach_date=time
        result.evaluation_method=met
        result.save()
        result=TeachPlan.objects.values().filter(department=jia1).filter(course=jia2)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response) 