from app1.models import *
from app1.util.utils import *

def delTeaching(request):
    '''
    url:
    http://127.0.0.1:8000/app7/delTeaching?teid=001&couid=100
    调用参数：
    老师工号：teid
    课程编号：couid
    教材名称：tbook

    '''
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            resdata = data["data"]
            Teid=resdata["teid"]
            Couid=resdata["couid"]
            Tbook=resdata["tbook"]
        # Teid=request.GET.get("teid")
        # Couid=request.GET.get("couid")
            result=Teaching.objects.filter(teacher_id=Teid).filter(curriculum_id=Couid).filter(textbook=Tbook).delete()
            result=Teaching.objects.all().values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)