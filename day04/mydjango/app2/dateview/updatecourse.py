from app1.models import Course
from app1.util.utils import *

def updateCourse(request):
    '''
    http://127.0.0.1:8000/app2/updateCourse?couid=001&couname=高等数学2&coubook=xxx
    '''
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            cid=data['couid']
            cName=data['couname']
            cbook=data['coubook']
        # cid=request.GET.get("couid")
        # cName=request.GET.get("couname")
        # cbook=request.GET.get("coubook")
            result=Course()
            result.cno=cid
            result.cname=cName
            result.textBook=cbook
            result.save()
            result=Course.objects.values().filter(cno=cid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)