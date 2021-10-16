from app1.models import *
from app1.util.utils import *

def addStudents(request):
    '''
    http://127.0.0.1:8000/app5/addStudents?sno=2019001&sname=张星新&sgender=女&studentDepartment__dno=002
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            for item in data:
                cid=item["sno"]
                coname=item["sname"]
                gender=item["sgender"]
                de=item["studentDepartment__dno"]
        # cid=request.GET.get("stid")
        # coname=request.GET.get("stname")
        # gender=request.GET.get("stgender")
        # de=request.GET.get("deid")
                deidd=Department.objects.get(dno=de)
                result=Student()
                result.sno=cid
                result.sname=coname
                result.sgender=gender
                result.studentDepartment=deidd
                result.save()
        result=Student.objects.all().values("sno","sname","sgender","studentDepartment__dno","studentDepartment__dname")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)