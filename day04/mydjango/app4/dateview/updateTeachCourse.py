from app1.models import *
from app1.util.utils import *

def updateTeachCourse(request):
    '''
        http://127.0.0.1:8000/app4/updateTeachCourse
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for datalist in data:
            

                tno=datalist["tno"]
                cno=datalist['teachCourse__cno']
                cname=datalist["teachCourse__cname"]
                Cno=Course.objects.get(cno=cno)
                Cname=Course.objects.get(cname=cname)
                Tno=Teacher.objects.get(tno=tno)
                Tno.teachCourse.remove(Cname)
                Tno.teachCourse.add(Cno)
            

            result=Teacher.objects.all().values('tno','tname','teachCourse__cno','teachCourse__cname')
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)