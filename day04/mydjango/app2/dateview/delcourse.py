from app1.models import Course
from app1.util.utils import *


def delCourse(request):
    '''
    http://127.0.0.1:8000/app2/delCourse?couid=001
    提交方式：POST
    参数：
        couid:课程编号
        {data:{couid:课程编号}}
    
    '''
    try:
         if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            cid=data['couid']
            # cName=data['couname']
        # cid=request.GET.get("couid")
            result=Course.objects.filter(cno=cid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
