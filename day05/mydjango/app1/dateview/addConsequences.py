from app1.models import *
from app1.util.utils import *

def addConsequences(request):
    '''
    url:
        http://127.0.0.1:8000/app1/addConsequences?couid=100&stid=2019002&sco=5.0&gdate=2001-08-16
    调用参数:
        couid:课程编号
        stid:学生编号
        sco:获得学分
        gdate:结课日期
    '''
    try:
        if(request.method =='POST'):
            condata=json.loads(request.body)
            data=condata["data"]
            for item in data:
                Cid=item["couid"]
                Sid=item["stid"]
                Sco=item["sco"]
                Gdate=item["gdate"]
                
        # Cid=request.GET.get("couid")
        # Sid=request.GET.get("stid")
        # Sco=request.GET.get("sco")
        # Gdate=request.GET.get("gdate")

                concou=Course.objects.get(cno=Cid)
                constu=Student.objects.get(sno=Sid)
                result=Consequence(subject=concou,student=constu,score=Sco,gain_date=Gdate)
                result.save()
        result=Consequence.objects.all().values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)