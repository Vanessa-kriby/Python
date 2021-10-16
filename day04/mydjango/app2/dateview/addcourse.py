    
from app1.models import Course
from app1.util.utils import *

def addCourses(request):
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            tid=data['couid']
            tName=data['couname']
            tbook=data['coubook']
        # tid=request.GET.get("cid")               
        # tname=request.GET.get("cname")                                                                                                           
            result=Course()
            result.cno=tid
            result.cname=tName
            result.textBook=tbook
            result.save()
            result=Course.objects.values().filter(cno=tid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
