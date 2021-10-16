from app1.util.utils import * 
from app1.models import *


def addTeachCourse(request):  #成功
    '''
        http://127.0.0.1:8000/app4/addTeachCourse
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
            for item in data:

                tno=item["tno"]
                cno=item['teachCourse__cno']
                tcourse=Course.objects.get(cno=cno)
                # tid=request.GET.get("teid")
            
                result=Teacher.objects.get(tno=tno)
                result.teachCourse.add(tcourse)

        result=Teacher.objects.all().values('tno','tname','teachCourse__cno','teachCourse__cname')
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)