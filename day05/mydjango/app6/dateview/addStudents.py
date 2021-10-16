from app1.models import *
from app1.util.utils import *

def addStudents(request):
    '''
    URL:
        http://127.0.0.1:8000/app6/addStudents?stid=2019002&stname=邓紫琪&stgender=女&deid=06
    调用参数：
        学生编号：stid
        学生姓名：stname
        教师性别：stgender
        学生专业：deid
    '''
    try:
         if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            for item in data:
                cid=item["stid"]
                coname=item["stname"]
                gender=item["stgender"]
                de=item["deid"]
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
            result=Student.objects.all().values("sno","sname","sgender","studentDepartment")
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
