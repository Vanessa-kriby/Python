from app1.models import *
from app1.util.utils import *

def addAdvance(request):
    '''
        get:
            http://127.0.0.1:8000/app1/addAdvance?ano=008&starttime=8:30:00&endtime=11:30:00&week=星期一&tno=001&crno=001&cno=001
        调用参数:
            ano:预排课表编号
            starttime:课程开始时间
            endtime:课程结束时间
            week:星期
            tno:工号
            crno:教室号
            cno:课程编号
        post:
            http://127.0.0.1:8000/app1/addAdvance
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for item in data:
        # aid=request.GET.get("ano")
        # st=request.GET.get("starttime")
        # en=request.GET.get("endtime")
        # we=request.GET.get("week")
        # tid=request.GET.get("tno")
        # crid=request.GET.get("crno")
        # cid=request.GET.get("cno")
                aid=item["ano"]
                st=item["starttime"]
                en=item["endtime"]
                we=item["week"]
                tid=item["tno"]
                crid=item["crno"]
                cid=item["cno"]

                Tno=Teacher.objects.get(tno=tid)
                Cron=Classroom.objects.get(crno=crid)
                Cno=Course.objects.get(cno=cid)
                result=Advance()
                result.ano=aid
                result.teacher=Tno
                result.classroom=Cron
                result.course=Cno
                result.week=we
                result.endtime=en
                result.starttime=st
                result.save()

        result=Advance.objects.all().values("starttime","endtime","week","teacher__tno","teacher__tname","classroom__crno","course__cno","course__cname")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)