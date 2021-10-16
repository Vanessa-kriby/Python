from app1.models import *
from app1.util.utils import *

def delStudent(request):
    '''
    http://127.0.0.1:8000/app5/delStudent?sno=2019002
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            sid=data["sno"]
            result=Student()
            result.sno=sid
            result=Student.objects.filter(sno=sid).delete()
            return showJsonresult(result)
        result=Student.objects.all().values("sno","sname","sgender","studentDepartment__dno","studentDepartment__dname")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)