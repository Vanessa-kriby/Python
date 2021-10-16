from app1.models import *
from app1.util.utils import *

def updateTeachPlan(request):
    try:
          if(request.method=='POST'):
            resdata=json.loads(request.body)
            datalist=resdata["data"]
            for data in datalist:
                co=data["cno"]
                gr=data["gno"]
                cr=data["credit"]
                tedate=data["teach_date"]
                check=data["checkType"]

                kco=Course.objects.get(cno=co)
                kgr=Grade.objects.get(gno=gr)

                result=TeachPlan.objects.filter(course=kco).filter(grade=kgr).update(credit=cr, teach_date=tedate,checkType=check)

            # result=TeachPlan()
            # result.course=kco
            # result.grade=kgr
            # result.credit=cr
            # result.teach_date=tedate
            # result.checkType=check
            # result.save()
          result=TeachPlan.objects.all().values('credit','teach_date','checkType','course__cno','course__cname','grade__gno','grade__gname')
          return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)