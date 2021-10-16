from app1.models import Student
from app1.util.utils import *

def delStudent(request):
    '''
        http://127.0.0.1:8000/app5/delStudent?stid=001
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            
            sid=data["stid"]

            result=Student.objects.filter(sno=sid).delete()
            result=Student.objects.all().values()
            
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)