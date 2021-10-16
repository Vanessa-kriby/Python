from app1.models import *
from app1.util.utils import *

def delConsequence(request):
    '''
    url：
        http://127.0.0.1:8000/app1/delConsequence?couid=100&stid=2019002
    '''
    try:
        if(request.method=='POST'):
            condata=json.loads(request.body)
            data=condata["data"]

            Cid=data["couid"]
            Sid=data["stid"]
            concou=Course.objects.get(cno=Cid)
            constu=Student.objects.get(sno=Sid)

            result=Consequence.objects.filter(subject_id=Cid).filter(student=Sid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
            
