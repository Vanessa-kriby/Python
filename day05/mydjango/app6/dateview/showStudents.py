from app1.models import *
from app1.util.utils import *

def showStudents(request):
    '''
    URL:
        http://127.0.0.1:8000/app6/showStudents?stid=2019001
    调用参数：
        学生编号：stid
    '''

    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            Sid=data["stid"]

            result=Student.objects.filter(sno=Sid).values("sno","sname","sgender","studentDepartment")
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
