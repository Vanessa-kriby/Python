from app1.models import Grade
from app1.util.utils import *

def addGrades(request):
    '''
    访问地址：
            http://127.0.0.1:8000/app1/addGrades?cid=5&cname=2021中医
    参数：
            班级编号：cid
            班级名称：cname
    '''
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            tid=data['cid']
            tName=data['cname']
        # tid=request.GET.get("cid")               
        # tname=request.GET.get("cname")                                                                                                           
            result=Grade()
            result.gno=tid
            result.gname=tName
            result.save()
            result=Grade.objects.values().filter(gno=tid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
