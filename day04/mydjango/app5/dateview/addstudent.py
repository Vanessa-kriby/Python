from app1.models import Student
from app1.util.utils import *

def addStudents(request):
    '''
        http://127.0.0.1:8000/app5/addStudents?sid=001&stName=邓紫棋
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            for item in data:
                tID=item["sid"]
                sName=item["stName"]
                sGender=item["stGender"]

                result=Student(sno=tID,sname=sName,gender=sGender)
                result.save()
            result=Student.objects.values().filter(sno=tID)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)