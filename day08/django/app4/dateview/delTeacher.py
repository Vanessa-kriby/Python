from app1.models import *
from app1.util.utils import *

def delTeacher(request):
    '''
    http://127.0.0.1:8000/app4/delTeacher?tno=107
    '''
    try:
        if(request.method=='POST'):
            data=json.loads(request.body)
            data=data["data"]
            tid=data["tno"]
        # tid=request.GET.get("tno")
            result=Teacher.objects.filter(tno=tid).delete()
        result=Teacher.objects.all().values("tno","tname","tgender","jobtitle")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)