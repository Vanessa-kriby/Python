from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from app1.models import *
import json
import datetime
from app1.comm.utils import *

def addStudents(request):
    '''
        http://127.0.0.1:8000/addStudents?sid=001&stName=邓紫棋&stGender=女
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]

            tID=data["sid"]
            sName=data["stName"]
            sGender=data["stGender"]

            result=Student(sno=tID,sname=sName,gender=sGender)
            result.save()
            result=Student.objects.values().filter(sno=tID)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def showStudents(request):
    '''
        http://127.0.0.1:8000/showStudents
    '''
    result=Student.objects.values().all()
    return showJsonresult(result)

def updateStudent(request):
    '''
        http://127.0.0.1:8000/updateStudent?sid=001&stName=林允儿&stGender=女
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]

            sID=data["sid"]
            sName=data["stName"]
            sGender=data["stGender"]

            result=Student.objects.get(sno=sID)
            result.sname=sName
            result.gender=sGender
            result.save()
            result=Student.objects.values().filter(sno=sID)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def delStudent(request):
    '''
        http://127.0.0.1:8000/delStudent?stid=001
    '''
    try:
        if(request.method=='POST'):
            studata=json.loads(request.body)
            data=studata["data"]

            sid=data["stid"]

            result=Student.objects.filter(sno=sid).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)