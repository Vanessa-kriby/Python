from app1.models import *
from app1.util.utils import *

def addPointsScoring(request):
    '''
        get:
            http://127.0.0.1:8000/app7/addPointsScoring?score=90&credit=2.0&tno=001&ino=1
        调用参数:
            score:分数
            credit:学分
            tno:教师
            ino:清单编号
        post:
            http://127.0.0.1:8000/app7/addPointsScoring
    '''
    try:
        if(request.method=='POST'):
           teadata=json.loads(request.body)
           data=teadata["data"]
           for item in data:
        # sco=request.GET.get("score")
        # cre=request.GET.get("credit")
        # tid=request.GET.get("tno")
        # iid=request.GET.get("ino")
                sco=item["score"]
                cre=item["credit"]
                tid=item["tno"]
                iid=item["ino"]

                Tno=Teacher.objects.get(tno=tid)
                Ino=Inventory.objects.get(ino=iid)
        
                result=PointsScoring()
                result.teacher=Tno
                result.inventory=Ino
                result.score=sco
                result.credit=cre
                result.save()

        result=PointsScoring.objects.all().values("inventory__student","inventory__teachPlan__course__cname","score","credit","teacher__tname")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)