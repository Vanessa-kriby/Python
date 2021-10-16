from app1.models import *
from app1.util.utils import *

def delTeachPlan(request):
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            co=data["cno"]
            gr=data["gno"]
            kco=Course.objects.get(cno=co)
            kgr=Grade.objects.get(gno=gr)
            TeachPlan.objects.filter(course=kco).filter(grade=kgr).delete()
            result=TeachPlan.objects.all().values('credit','teach_date','checkType','course__cno','course__cname','grade__gno','grade__gname')
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)   