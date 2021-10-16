from app1.models import *
from app1.util.utils import *

def updateAdvance(request):
    '''
        get:
            http://127.0.0.1:8000/app1/updateAdvance?ano=007&starttime=8:30&endtime=11:30&week=星期一
        调用参数:
            ano:预排课表编号
            starttime:课程开始时间
            endtime:课程结束时间
            week:星期
        post:
            http://127.0.0.1:8000/app1/updateAdvance
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

                aid=item["ano"]
                st=item["starttime"]
                en=item["endtime"]
                we=item["week"]

                result=Advance.objects.filter(ano=aid).update(starttime=st,endtime=en,week=we)

        result=Advance.objects.all().values("starttime","endtime","week","teacher__tno","teacher__tname","classroom__crno","course__cno","course__cname")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)