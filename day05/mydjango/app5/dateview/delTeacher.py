from app1.models import *
from app1.util.utils import *

def delTeacher(request):
    '''
    URL：
        http://127.0.0.1:8000/app5/delTeacher?teid=001
    调用参数：
        教师编号：teid
        
    '''
    try:
        if(request.method=='POST'):
            tdata=json.loads(request.body)
            data=tdata["data"]
            
            cid=data['teid']
        # cid=request.GET.get("stid")
            result=Student()
            result.sno=cid
            result=Teacher.objects.filter(tno=cid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)