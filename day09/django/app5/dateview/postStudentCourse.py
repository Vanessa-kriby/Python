from app1.models import *
from app1.util.utils import *

def postStudentCourse(request):
    '''
        http://127.0.0.1:8000/app5/postStudentCourse
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            sno=data['sno']
            tno=data['tno']
            tpnos=data['tpnos']
            
            teacherobj=Teacher.objects.get(tno=tno)
            teachPlanobj=TeachPlan.objects.get(tpno=tpnos)
            studentobj=Student.objects.get(sno=sno)
            Inventory.objects.create(teacher=teacherobj,teachPlan=teachPlanobj,student=studentobj,ino=tpnos,select_date='2020-01-23')
            # for item in data['tpnos','tno']:
            #     cno=item
            #     courseobj=Course.objects.get(cno=cno)
            #     Achievement.objects.create(course=courseobj,student=studentobj,score=0.0,gain_date='2025-12-31')

        
        response={}
        response['msg']='good job'
        response['err_num']=0
        response['data']=''
        return JsonResponse(response, safe=False)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)