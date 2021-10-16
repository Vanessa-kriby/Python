from app1.models import *
from app1.util.utils import *

def delTeachCourse(request):
    '''
        http://127.0.0.1:8000/app5/delTeachCourse?tno=001&teachCourse__cno
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]
            
            tno=data["tno"]
            teachCourse__cno=data['teachCourse__cno']

            teacherobj=Teacher.objects.get(tno=tno)
            courseobj=Course.objects.get(cno=teachCourse__cno)
            teacherobj.teachCourse.remove(courseobj)
            
            return showJsonresult(teacherobj)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)