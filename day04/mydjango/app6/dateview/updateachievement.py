from app1.models import *
from app1.util.utils import *

def updateAchievement(request):
    '''
    http://127.0.0.1:8000/updateAchievement
    '''
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            resdata = data["data"]
            couid=resdata["cid"]
            stuid=resdata["sid"]
            Sco=resdata["sco"]
            Gain=resdata["gaindata"]
            former=Achievement.objects.get(student_id=stuid,course_id=couid)
            former.delete()
            astudent=Student.objects.get(sno=stuid)
            acourse=Course.objects.get(cno=couid)
            result=Achievement()
            result.course=acourse
            result.student=astudent
            result.gain_date=Gain
            result.score=Sco
            result.save()
            result=Achievement.objects.values().filter(student_id=stuid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
