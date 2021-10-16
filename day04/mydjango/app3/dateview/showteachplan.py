from app1.models import *
from app1.util.utils import *

def showTeachPlans(request):
        try:

                result=TeachPlan.objects.all().values('credit','teach_date','checkType','course__cno','course__cname','grade__gno','grade__gname')
                return showJsonresult(result)
        except Exception as e:
                response={}
                response['msg']=str(e)
                response['err_num']=1
                return showJsonerror(response)
