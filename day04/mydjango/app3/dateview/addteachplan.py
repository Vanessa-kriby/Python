from app1.models import *
from app1.util.utils import *

'''
http://127.0.0.1:8000/app3/addTeachPlans?cid=001&gra=1&cri=3&teadate=2019-01-01&checktype=考试
'''

def addTeachPlans(request):


    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            for index in data:
                co=index["cno"]
                gr=index["gno"],""
                cr=index["credit"]
                tedate=index["teach_date"]
                check=index["checkType"]
    
                kco=Course.objects.get(cno=co) 
                kgr=Grade.objects.get(gno=gr)
                result=TeachPlan()
                result.course=kco
                result.grade=kgr
                result.credit=cr
                result.teach_date=tedate
                result.checkType=check
                result.save()

        result=TeachPlan.objects.all().values('credit','teach_date','checkType','course__cno','course__cname','grade__gno','grade__gname')
        return showJsonresult(result)    
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)