from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ..models import * 
import json
import datetime
from app1.comm.utils import *
# from ..communal import communal   #直接导入模型是不行的 要导入具体的函数
# from ..communal.communal import * 


def addTeachers(request):
    '''
        http://127.0.0.1:8000/addTeachers?teid=x&teName=x&teGender=x&tejobTitle=x
    '''
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]

            tid=data["teid"]
            tName=data["teName"]
            tgender=data["teGender"]
            tjt=data["tejobTitle"]
            result=Teacher()
            result.tno=tid
            result.tname=tName
            result.gender=tgender
            result.jobTitle=tjt
            result.save()
            result=Teacher.objects.values().filter(tno=tid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)


def showTeachers(request):
    '''
        http://127.0.0.1:8000/showTeachers
    '''
    result=Teacher.objects.all().values()
    return showJsonresult(result)

def delTeacher(request):
    try:
        if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]

            tid=data["teid"]
            t1=Teacher.objects.get(tno=tid)

            result=Teacher.objects.values().filter(tno=tid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def teaching(request):
    try:
         if(request.method=='POST'):
            teadata=json.loads(request.body)
            data=teadata["data"]

            tid=data["teid"]
            cid=data["couid"]
            t1=Teacher.objects.get(tno=tid)
            c1=Course.objects.get(cno=cid)
            t1.teachCourse.add(c1)
            result=Teacher.objects.values("tno","teachCourse").filter(tno=tid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)