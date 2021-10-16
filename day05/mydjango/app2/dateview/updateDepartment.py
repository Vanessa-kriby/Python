from app1.models import *
from app1.util.utils import *


def updateDepartment(request):
    '''
    url:
        http://127.0.0.1:8000/app2/updateDepartment?deid=01&dename=xxx
    调用参数:
        deid:专业编号
        dename:专业名称
    '''
    try:
          if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            decouid=data["deid"]
            deName=data["dename"]
        # decouid=request.GET.get("deid")
        # deName=request.GET.get("dename")
            result=Department()
            result.dno=decouid
            result.dname=deName
            result.save()
            result=Department.objects.all().values()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)