from app1.models import *
from app1.util.utils import *

'''
url:
    http://127.0.0.1:8000/app2/addDepartments?deid=01&dename=计算机科学与技术
调用参数：
    deid:专业编号
    dename:专业名称
'''

def addDepartments(request):
   
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            for item in data:
                decouid=item["deid"]
                deName=item["dename"]
                # decouid=request.GET.get("deid")
                # deName=request.GET.get("dename")
                result=Department()
                result.dno=decouid
                result.dname=deName
                result.save()
            result=Department.objects.filter(dno=decouid).values()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)