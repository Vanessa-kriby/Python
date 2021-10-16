from app1.models import *
from app1.util.utils import *

def delTeacher(request):
    '''
        get:
            http://127.0.0.1:8000/app3/delTeacher?tno=001
        post:
            http://127.0.0.1:8000/app3/delTeacher
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
        # tid=request.GET.get("tno")
        
            tid=data["tno"]

            result=Teacher.objects.filter(tno=tid).delete()

        result=Teacher.objects.values().all()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)