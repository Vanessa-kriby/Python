from app1.models import *
from app1.util.utils import *

def updateInventory(request):
    '''
        http://127.0.0.1:8000/app6/updateInventory?ino=001&select_date=2020-7-9&teachPlan=001&teacher=101&student=2019001
    '''
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            data = resdata["data"]
            for index in data:
                ino = index['inid']
                select_date = index['sdate']
                teachPlan = index['tpid']
                teacher = index['stid']
                student = index['stid']
        # ino = request.GET.get("ino")
        # select_date = request.GET.get("select_date")
        # teachPlan = request.GET.get("teachPlan")                   #暂时等级查询不到
        # teacher = request.GET.get("teacher")                     #暂时等级查询不到
        # student = request.GET.get("student")                     #暂时等级查询不到
                tpno = TeachPlan.objects.get(tpno=teachPlan)       
                tno = Teacher.objects.get(tno=teacher)
                sno = Student.objects.get(sno=student)
                result = Inventory.objects.filter(ino=ino).update(teacher=tno)
        result = Inventory.objects.values('ino','teachPlan__department__dname','student__sno','student__sname','teachPlan__course__cname','teacher__tname','select_date')
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)