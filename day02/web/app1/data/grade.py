from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
from app1.comm.utils import *
import json
import datetime


def addGrades(request):
    '''
    http://127.0.0.1:8000/addGrades?cid=1&cname=2019计科
    '''
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            id=data['cid']
            tname=data['cname']
            result=Grade(gname=tname)
            result.gno=id
            result.save()
            result=Grade.objects.values().filter(gname=tname)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def showGrades(request):
    '''
    http://127.0.0.1:8000/showGrades
    '''
    result=Grade.objects.all().values()
    return showJsonresult(result)

def delGrade(request):
    '''
    http://127.0.0.1:8000/delGrade?gid=1
    '''
    try:
         if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            id=data['gid']
            # tname=data['cname']
            result=Grade.objects.filter(gno=id).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def updateGrade(request):
    '''
    http://127.0.0.1:8000/updateGrade?gid=1&gname=2019计科
    '''
    try:
        cid=request.GET.get("gid")
        cName=request.GET.get("gname")
        result=Grade.objects.get(gno=cid)
        result.gname=cName
        result.save()
        result=Grade.objects.values().filter(gno=cid)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

