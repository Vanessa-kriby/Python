from app1.models import *
from app1.util.utils import *

def addInventorys(request):
    '''
        get:
            http://127.0.0.1:8000/app6/addInventorys?ino=001&tpno=001&sno=001
        调用函数:
            ino:清单编号
            select_date:选课日期
            tpno:计划编号
            sno:学号
        post:
            http://127.0.0.1:8000/app6/addInventorys
    '''
    try:
        if(request.method=='POST'):
           invdata=json.loads(request.body)
           data=invdata["data"]
           for item in data:
        # iid=request.GET.get("ino")
        # sed=request.GET.get("select_date")
        # tpid=request.GET.get("tpno")
        # sid=request.GET.get("sno")

                iid=item["ino"]
                # sed=item["select_date"]
                tpid=item["tpno"]
                sid=item["sno"]

                Tpid=TeachPlan.objects.get(tpno=tpid)
                Sid=Student.objects.get(sno=sid)
                result=Inventory()
                result.ino=iid
                # result.select_date=sed
                result.teachPlan=Tpid
                result.student=Sid
                result.save()

        result=Inventory.objects.all().values("ino","select_date","teachPlan__tpno","student__sno")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)