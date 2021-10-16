from app1.models import *
from app1.util.utils import *


def updateGrade(request):
    '''
    http://127.0.0.1:8000/app1/updateGrade?gid=xxx&gname=xxxx
    '''
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            tid=data['gid']
            tName=data['gname']
        # tid=request.GET.get("cid")               
        # tname=request.GET.get("cname")                                                                                                           
            result=Grade()
            result.gno=tid
            result.gname=tName
            result.save()
            result=Grade.objects.values().filter(gno=tid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)