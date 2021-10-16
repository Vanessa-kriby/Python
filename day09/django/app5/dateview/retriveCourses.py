from app1.models import *
from app1.util.utils import *


def retriveCourses(request):
    '''
    http://127.0.0.1:8000/app5/retriveCourses?tpno=101
    '''
    try:
        teachPlan = request.GET.get('tpno')
        resultPlanCourse = TeachPlan.objects.all().values("course__cno","course__cname","teacher__tno",).filter(tpno=teachPlan)
        return showJsonresult(resultPlanCourse)
        # result=TeachPlan.objects.values().get(tpno=teachPlan)
        # response={}
        # response['msg']='good job'
        # response['err_num']=0
        # response['data']=result
        # return JsonResponse(response, safe=False)
        # teachPlanpiont = TeachPlan(tpno=teachPlan)
        # result=Course.objects.all().filter(teachplan__teach_date__gte="2010-01-01").values()
        # resultTeachPlanCourse=Inventory.objects.all().filter(teachPlan__tpno=teachPlan).values()
        # result =Course.objects.all().filter(teacher__tno__isnull=False).filter(teachplan__teach_date__gte="2020-01-01").values("cno","cname","teacher__tno","teacher__tname","teachplan__credit")
        # resultPlanCourse=TeachPlan.objects.all().values().filter(tpno=teachPlan)
        # return showJsonresult(result)
    except Exception as e:
        response = {}
        response['msg'] = str(e)
        response['err_num'] = 1
        return showJsonerror(response)
