from app1.models import *
from app1.util.utils import *

def delAdvance(request):
    '''
        get:
            http://127.0.0.1:8000/app1/delAdvance?ano=007
        调用参数:
            ano:预排课表编号
        post:
            http://127.0.0.1:8000/app1/delAdvance
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]
        # aid=request.GET.get("ano")

            aid=data["ano"]

            result=Advance.objects.filter(ano=aid).delete()

        result=Advance.objects.all().values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)