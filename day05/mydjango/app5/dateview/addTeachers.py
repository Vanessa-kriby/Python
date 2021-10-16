
from app1.models import *
from app1.util.utils import *

def addTeachers(request):
    '''
    URL:
    http://127.0.0.1:8000/app5/addTeachers?teid=005&tename=王俊凯&tegender=男&tejob=教授
    调用参数：
        教师编号：teid
        教师姓名：tename
        教师性别：tegender
        教师职称：tejob

    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for item in data:
                cid=item["teid"]
                coname=item["tename"]
                gender=item["tegender"]
                tjob=item["tejob"]
        # cid=request.GET.get("teid")
        # coname=request.GET.get("tename")
        # gender=request.GET.get("tegender")
        # tjob=request.GET.get("tejob")
                result=Teacher()
                result.tno=cid
                result.tname=coname
                result.tgender=gender
                result.jobtitle=tjob
                result.save()
            result=Teacher.objects.values().filter(tno=cid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
