from app1.models import *
from app1.util.utils import *

def postStudentCourse(request):
    '''
        get:
            http://127.0.0.1:8000/app5/postStudentCourse?sno=001&tpno=001
        调用参数:
            sno:学号
            tpno:计划编号
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]

            sno=data['sno']
            studentobj=Student.objects.get(sno=sno)
            for item in data['cons']:
            # for item in data:
                tpno=item
                teachplanobj=TeachPlan.objects.get(tpno=tpno)
                Inventory.objects.create(student=studentobj,teachPlan=teachplanobj)
        
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