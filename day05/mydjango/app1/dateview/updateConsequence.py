from app1.models import *
from app1.util.utils import *

def updateConsequence(request):
    '''
    url:
        http://127.0.0.1:8000/app1/updateConsequence?nsid=2019002&couid=100&stid=2019002&sco=3.0&gdate=2001-08-22
    调用参数:
        couid:课程编号
        stid:学生编号
        sco:获得学分
        gdate:结课日期
    '''
    try:
        if(request.method=='POST'):
            condata=json.loads(request.body)
            data=condata["data"]

            Newsid=data["newstid"]
            Cid=data["couid"]
            Sid=data["stid"]
            Sco=data["sco"]
            Gdate=data["gdate"]

        # nSid=request.GET.get("nsid")
        # Cid=request.GET.get("couid")
        # Sid=request.GET.get("stid")
        # Sco=request.GET.get("sco")
        # Gdate=request.GET.get("gdate")

            concou=Course.objects.get(cno=Cid)
            constu=Student.objects.get(sno=nSid)
            cresult=Consequence.objects.filter(subject=Cid).filter(student=Sid).delete()
            result=Consequence()
            result.subject=concou
            result.student=constu
            result.score=Sco
            result.gain_date=Gdate
            result.save()
        result=Consequence.objects.values().filter(subject=Cid).filter(student=nSid)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)