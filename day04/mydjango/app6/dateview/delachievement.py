from app1.models import *
from app1.util.utils import *

def delAchievement(request):
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            resdata = data["data"]
            stuid=resdata["sid"]
            couid=resdata["cid"]
            tresult=Achievement.objects.filter(student_id=stuid).filter(course_id=couid).delete()
        return showJsonresult(tresult)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)