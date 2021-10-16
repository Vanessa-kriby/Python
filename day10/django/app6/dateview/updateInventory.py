from app1.models import *
from app1.util.utils import *

def updateInventory(request):
    '''
        get:
            http://127.0.0.1:8000/app6/updateInventory?ino=001&select_date=2019-12-24
        post:
            http://127.0.0.1:8000/app6/updateInventory
    '''
    try:
        if(request.method=='POST'):
           teadata=json.loads(request.body)
           data=teadata["data"]
           for item in data:
        # iid=request.GET.get("ino")
        # sed=request.GET.get("select_date")
        # tpid=request.GET.get("tpno")
        # sid=request.GET.get("sno")

                iid=item["ino"]
                sed=item["select_date"]
                # tpid=item["tpno"]
                # sid=item["sno"]

                # Tpid=TeachPlan.objects.get(tpno=tpid)
                # Sid=Student.objects.get(sno=sid)

                result=Inventory.objects.filter(ino=iid).update(select_date=sed)

        result=Inventory.objects.all().values("ino","select_date","teachPlan__tpno","student__sno")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)