from app1.models import *
from app1.util.utils import *


def retriveTeachPlans(request):
    '''
    http://127.0.0.1:8000/app5/retriveTeachPlans?tpno=101
    '''
    try:
        teachPlan = request.GET.get('tpno')
        # result=Course.objects.all().filter(teachplan__teach_date__gte="2010-01-01").values()
        # resultStudentCourse=Inventory.objects.filter(teachPlan__tpno=teachPlan).values("teachPlan__course__cno","teachPlan__tpno")
        # result =Course.objects.all().filter(teacher__tno__isnull=False).filter(teachplan__teach_date__gte="2020-01-01").values("cno","cname","teacher__tno","teacher__tname","teachplan__credit")
        resultPlanCourse=TeachPlan.objects.all().values("tpno","course__cno",).filter(tpno=teachPlan)
        # for item in resultStudentCourse:
        #     resultPlanCourse=resultPlanCourse.exclude(tpno=item[teachPlan])
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