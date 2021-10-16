from app1.models import *
from app1.util.utils import *

def showTeachings(request):
    '''
    url:
    http://127.0.0.1:8000/app7/showTeachings?teid=002&couid=002
    调用参数：
    老师工号：teid
    课程编号：couid
    '''
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            data = data["data"]
            Teid=data["teid"]
            Couid=data["couid"]
            result=Teaching.objects.filter(teacher_id=Teid).filter(curriculum_id=Couid).values('teacher_id','curriculum_id','textbook')
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)