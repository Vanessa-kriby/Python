from app1.models import *
from app1.util.utils import *

def updateTeacher(request):
    '''
        get:
            http://127.0.0.1:8000/app3/updateTeacher?tno=001&tname=叶茹雪&tgender=女&jobtitle=讲师
        调用参数:
            tno:工号
            tname:姓名
            tgender:性别
            jobtitle:职称
        post:
            http://127.0.0.1:8000/app3/updateTeacher
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for item in data:
        # tid=request.GET.get("tno")
        # tna=request.GET.get("tname")
        # tge=request.GET.get("tgender")
        # job=request.GET.get("jobtitle")
                tid=item["tno"]
                tna=item["tname"]
                tge=item["tgender"]
                job=item["jobtitle"]

                result=Teacher.objects.filter(tno=tid).update(tname=tna,tgender=tge,jobtitle=job)

        result=Teacher.objects.all().values("tno","tname","tgender","jobtitle")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)