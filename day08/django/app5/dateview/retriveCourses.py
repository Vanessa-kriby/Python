from app1.models import *
from app1.util.utils import *


def retriveCourses(request):
    '''
    http://127.0.0.1:8000/app5/retriveCourses?sno=2019001
    '''
    try:
        stuNum = request.GET.get('sno')
        result=Course.objects.all().filter(teachplan__teach_date__gte="2010-01-01").values()
        resultStudentCourse=Department.objects.filter(student__sno=stuNum).values("course__cno")
        result =Course.objects.all().filter(teacher__tno__isnull=False).filter(teachplan__teach_date__gte="2020-01-01").values("cno","cname","teacher__tno","teacher__tname","teachplan__credit")
        resultPlanCourse=Course.objects.all().values()
        for item in resultStudentCourse:
            resultPlanCourse=resultPlanCourse.exclude(cno=item['course__cno'])
        response = {}
        response['msg'] = "Success"
        response['err_num'] = 0
        response['data'] = list(resultPlanCourse)

    # result=Course.objects.all().filter(teacher__tno__isnull=False).filter(teachplan__teach_date__gte="2020-01-01").values()
        return JsonResponse(response)
        return showJsonresult(result,safe=False)
    except Exception as e:
        response = {}
        response['msg'] = str(e)
        response['err_num'] = 1
        return showJsonerror(response)
