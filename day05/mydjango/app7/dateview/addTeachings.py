from app1.models import *
from app1.util.utils import *

def addTeachings(request):
    '''
    url：
    http://127.0.0.1:8000/app7/addTeaching?teid=001&couid=100&tbook=浙江大学出版社9877
    调用参数：
    老师工号：teid
    课程编号：couid
    教材名称：tbook
    '''
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            data = data["data"]
            for item in data:
                Teid=item["teid"]
                Couid=item["couid"]
                Tbook=item["tbook"]
        # Teid=request.GET.get("teid")
        # Tbook=request.GET.get("tbook")
        # Couid=request.GET.get("couid")
                ateacher=Teacher.objects.get(tno=Teid)
                acourse=Course.objects.get(cno=Couid)
                result=Teaching()
                result.teacher=ateacher
                result.curriculum=acourse
                result.textbook=Tbook
                result.save()
        result=Teaching.objects.values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)