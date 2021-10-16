from app1.models import *
from app1.util.utils import *

def addTeachers(request):
    '''
    http://127.0.0.1:8000/app4/addTeachers?tno=107&tname=张星新&tgender=女&jobtitle=教授
    '''
    try:
        if(request.method=='POST'):
            data=json.loads(request.body)
            data=data["data"]
            for item in data:
                tid=item["tno"]
                tName=item["tname"]
                tgen=item["tgender"]
                tjob=item["jobtitle"]
        # tid=request.GET.get("tno")
        # tName=request.GET.get("tname")
        # tgen=request.GET.get("tgender")
        # tjob=request.GET.get("jobtitle")
                result=Teacher()
                result.tno=tid
                result.tname=tName
                result.tgender=tgen
                result.jobtitle=tjob
                result.save()
        result=Teacher.objects.all().values("tno","tname","tgender","jobtitle")
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)