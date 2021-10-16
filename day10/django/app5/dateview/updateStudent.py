from app1.models import *
from app1.util.utils import *

def updateStudent(request):
    '''
        get:
            http://127.0.0.1:8000/app5/updateStudent?sno=001&sname=邓紫棋&sgender=女&nation=汉族&native_place=中国上海&studentDepartment__studentDepartment__dno=001
        调用参数:
            sno:学号
            sname:姓名
            sgender:性别
            nation:种族
            native_place:籍贯
            studentDepartment__dno:专业编号
        post:
            http://127.0.0.1:8000/app5/updateStudent
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            for item in data:
        # sid=request.GET.get("sno")
        # sna=request.GET.get("sname")
        # sge=request.GET.get("sgender")
        # nat=request.GET.get("nation")
        # nap=request.GET.get("native_place")
        # did=request.GET.get("studentDepartment__dno")

                sid=item["sno"]
                sna=item["sname"]
                sge=item["sgender"]
                nat=item["nation"]
                nap=item["native_place"]
                did=item["studentDepartment__dno"]

                result=Student.objects.filter(sno=sid).update(sname=sna,sgender=sge,nation=nat,native_place=nap)

        result=Student.objects.all().values("sno","sname","sgender","nation","native_place")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)