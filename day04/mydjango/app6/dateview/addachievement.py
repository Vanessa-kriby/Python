from app1.models import *
from app1.util.utils import *

def addAchievements(request):
    '''
    http://127.0.0.1:8000/addAchievements?cid=001&sid=20190002&sco=3&gain=2020-7-9
    '''
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            resdata = data["data"]
            couid=resdata["cid"]
            stuid=resdata["sid"]
            Sco=resdata["sco"]
            Gain=resdata["gaindata"]
            astudent=Student.objects.get(sno=stuid)
            acourse=Course.objects.get(cno=couid)
            result=Achievement()
            result.course=acourse
            result.student=astudent
            result.score=Sco
            result.gain_date=Gain
            result.save()
            result=Achievement.objects.values().filter(student_id=stuid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)