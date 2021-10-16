from app1.models import *
from app1.util.utils import *

def delTeacher(request):
    '''
    URL：
        http://127.0.0.1:8000/app4/delTeacher?tno=xxx
    调用参数：
        教师编号：tno
        
    '''
    try:
        if(request.method=='POST'):
            tdata=json.loads(request.body)
            data=tdata["data"]
            tid=data['tno']
            result=Teacher.objects.filter(tno=tid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)