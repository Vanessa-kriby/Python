from app1.models import *
from app1.util.utils import *

def showConsequences(request):
    '''
    url:
        http://127.0.0.1:8000/app1/showConsequences?couid=100&stid=2019002
    参数:
        couid:课程编号
        stid:学生编号
    '''
    try:
        if(request.method =='POST'):
            condata=json.loads(request.body)
            data=condata["data"]

            Cid=data["couid"]
            Sid=data["stid"]

        # Cid=request.GET.get("couid")
        # Sid=request.GET.get("stid")

        result=Consequence.objects.filter(subject=Cid).filter(student=Sid).values()
        return showJsonresult(result)

    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)