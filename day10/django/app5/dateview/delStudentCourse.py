from app1.models import *
from app1.util.utils import *

def delStudentCourse(request):
    '''
        get:
            http://127.0.0.1:8000/app5/delStudentCourse?ino=2
        调用参数:
            ino:清单编号
        post:
            http://127.0.0.1:8000/app5/delStudentCourse
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            
        # iid=request.GET.get("ino")
            iid=data["ino"]

            result=Inventory.objects.filter(ino=iid).delete()
            
        result=Inventory.objects.values().all()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)