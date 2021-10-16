from app1.models import *
from app1.util.utils import *

def updateTeaching(request):
    '''
    url:
        http://127.0.0.1:8000/app7/updateTeaching?teid=001&couid=100&tbook=浙江大学出版社9899
    调用参数：
        老师工号：teid
        课程编号：couid
        教材名称：tbook
    '''
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            resdata = data["data"]
            for item in data:
                Teid=resdata["teid"]
                Couid=resdata["couid"]
                Tbook=resdata["tbook"]
        # result.curriculum_id=acourse
        # result.teacher_id=ateacher
        # Teid=request.GET.get("teid")
        # Tbook=request.GET.get("tbook")
        # Couid=request.GET.get("couid")
                ateacher=Teacher.objects.get(tno=Teid)
                acourse=Course.objects.get(cno=Couid)
                result=Teaching.objects.filter(curriculum=acourse).filter(teacher=ateacher).filter(textbook=Tbook).delete()
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