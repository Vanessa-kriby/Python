from app1.models import *
from app1.util.utils import *

def delStudent(request):
    '''
    URL:
        http://127.0.0.1:8000/app6/delStudent?stid=2019003
    调用参数：
        学生编号：stid
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            
            cid=data['stid']
        # cid=request.GET.get("stid")
            result=Student()
            result.sno=cid
            result=Student.objects.filter(sno=cid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)