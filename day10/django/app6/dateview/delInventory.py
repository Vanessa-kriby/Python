from app1.models import *
from app1.util.utils import *

def delInventory(request):
    '''
        get:
            http://127.0.0.1:8000/app6/delInventory?ino=001
        post:
            http://127.0.0.1:8000/app6/delInventory 
    '''
    try:
        if(request.method=='POST'):
            invdata=json.loads(request.body)
            data=invdata["data"]
        # iid=request.GET.get("ino")

            iid=data["ino"]

            result=Inventory.objects.filter(ino=iid).delete()

        result=Inventory.objects.all().values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)