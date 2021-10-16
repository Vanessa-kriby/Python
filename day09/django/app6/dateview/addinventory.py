from app1.models import *
from app1.util.utils import *

def addInventorys(request):
    '''
        http://127.0.0.1:8000/app6/addInventorys?init=001&sdate=2020-7-9&tpid=001&stid=101&stid=2019001
    '''
    try:
        if(request.method=='POST'):
            resdata = json.loads(request.body)
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
                result = Inventory()
                result.ino = ino
                result.select_date = select_date
                result.teachPlan = tpno
                result.teacher = tno
                result.student = sno
                result.save()
        result = Inventory.objects.values('ino','teachPlan__department__dname','student__sno','student__sname','teachPlan__course__cname','teachPlan__teacher__tname','select_date').filter(ino=ino)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)