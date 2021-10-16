from app1.models import Student
from app1.util.utils import *

def updateStudent(request):
    '''
        http://127.0.0.1:8000/app5/updateStudent?sid=001&stName=林允儿&stGender=女
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]

            sID=data["sid"]
            sName=data["stName"]
            sGender=data["stGender"]
            result=Student.objects.get(sno=sID)
            result.sname=sName
            result.gender=sGender
            result.save()
            result=Student.objects.values().filter(sno=sID)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)