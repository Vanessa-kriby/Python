from app1.models import *
from app1.util.utils import *

def addTeachers(request):
    '''
    URL:
    http://127.0.0.1:8000/app4/addTeachers?tno=107&tname=张星新&tgender=女&jobtitle=教授
    调用参数：
        教师编号：tno
        教师姓名：tname
        教师性别：tgender
        教师职称：jobtitle

    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for item in data:
                tid=item["tno"]
                tName=item["tname"]
                tgen=item["tgender"]
                tjob=item["jobtitle"]
                result=Teacher()
                result.tno=tid
                result.tname=tName
                result.tgender=tgen
                result.jobtitle=tjob
                result.save()
            result=Teacher.objects.values().filter(tno=tid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)