from app1.models import *
from app1.util.utils import *

def retriveCourse(request):
    '''
        http://127.0.0.1:8000/app5/retriveCourse
    '''
    try:
        stuNum=request.GET.get('studentNum')
        # result=Course.objects.all().filter(teachplan__teach_date__gte ="2020-01-01").values()
        resultStudentCourse=Achievement.objects.filter(student__sno=stuNum).values("course__cno")
        # resultPlanCourse=Course.objects.all().filter(teacher__tno__isnull=False).filter(teachplan__teach_date__gte ="2020-01-01").values("cno","cname","teacher__tno","teacher__tname","teachplan__credit")
        resultPlanCourse=Course.objects.all().values("cno","cname","teacher__tno","teacher__tname","teachplan__credit")
        # for item in resultStudentCourse:
            # resultPlanCourse=resultPlanCourse.exclude(cno=item['course__cno'])
        # response={}
        # response['msg']='good job'
        # response['err_num']=0
        # response['data']=list(resultPlanCourse)
        # return JsonResponse(response, safe=False)
        return showJsonresult(resultPlanCourse)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
    