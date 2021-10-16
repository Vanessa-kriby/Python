from app1.models import *
from app1.util.utils import *

def delInventory(request):
    '''
        http://127.0.0.1:8000/app6/delInventory?ino=001
    '''
    try:
        if(request.method=='POST'):
            resdata = json.loads(request.body)
            data = resdata["data"]
            inid = data['ino']
        # inid = request.GET.get("ino")
            result = Inventory.objects.filter(ino=inid).delete()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)