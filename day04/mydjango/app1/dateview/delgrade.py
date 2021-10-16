from app1.models import Grade
from app1.util.utils import *

def delGrade(request):
    '''
    http://127.0.0.1:8000/app1/delGrade?gid=2
    '''
    try:
         if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            id=data['gid']
        # tid=request.GET.get("gid")
            result=Grade.objects.filter(gno=id).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
