from app1.models import *
from app1.util.utils import *

def showTeachers(request):
    '''
    URL:
        http://127.0.0.1:8000/app5/showTeachers?teid=005
    调用参数：
        教师编号：teid
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            Sid=data["teid"]

            result=Teacher.objects.filter(tno=Sid).values("tno","tname","tgender","jobtitle")
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
