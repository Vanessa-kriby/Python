from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
from app1.comm.utils import *
import json
import datetime

def addCourses(request):
    '''
    http://127.0.0.1:8000/addCourses?couid=001&couname=高等数学1&coubook=xxx
    '''
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            cid=data['couid']
            cName=data['couname']
            cbook=data['coubook']
            result=Course()
            result.cno=cid
            result.cname=cName
            result.textBook=cbook
            result.save()
            result=Course.objects.values().filter(cno=cid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def showCourses(request):
    '''
    http://127.0.0.1:8000/showCourses
    '''
    result=Course.objects.all().values("cname","cno","textBook")
    return showJsonresult(result)

def delCourse(request):
    '''
    http://127.0.0.1:8000/delCourse?couid=001
    '''
    try:
         if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            cid=data['couid']
            # cName=data['couname']
            result=Course.objects.filter(cno=cid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def updateCourse(request):
    '''
    http://127.0.0.1:8000/updateCourse?couid=001&couname=高等数学1&coubook=xxx
    '''
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            cid=data['couid']
            cName=data['couname']
            cbook=data['coubook']
            result=Course()
            result.cno=cid
            result.cname=cName
            result.textBook=cbook
            result.save()
            result=Course.objects.values().filter(cno=cid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

