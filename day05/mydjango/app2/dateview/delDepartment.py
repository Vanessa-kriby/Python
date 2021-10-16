from app1.models import *
from app1.util.utils import *


def delDepartment(request):
    '''
    url：
    http://127.0.0.1:8000/app2/delDepartment?deid=xxx
    调用参数：
        deid:专业编号
    '''
    try:
          if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            decouid=data["deid"]
        # decouid=request.GET.get("deid")
            result=Department.objects.filter(dno=decouid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)