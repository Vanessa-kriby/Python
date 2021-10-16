from app1.models import *
from app1.util.utils import *

def updatePointsScoring(request):
    '''
        get:
            http://127.0.0.1:8000/app7/updatePointsScoring?score=80&credit=1.0
        post:
            http://127.0.0.1:8000/app7/updatePointsScoring
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for item in data:
        # sco=request.GET.get("score")
        # cre=request.GET.get("credit")

                sco=item["score"]
                cre=item["credit"]

            result=PointsScoring.objects.filter().update(credit=cre,score=sco)

            result=PointsScoring.objects.all().values("inventory__student","inventory__teachPlan__course__cname","score","credit","teacher__tname")
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)