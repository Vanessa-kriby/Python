from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# from .models import *
from django.core import serializers
import json
import datetime
from app1.models import *
# from .utils import *
from app1.comm.utils import *

def addAchievements(request):
    '''
    http://127.0.0.1:8000/addAchievements?cid=001&sid=20190002&sco=3&gain=2020-7-9
    '''
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            resdata = data["data"]
            couid=resdata["cid"]
            stuid=resdata["sid"]
            Sco=resdata["sco"]
            Gain=resdata["gaindata"]
            # couid=request.GET.get("cid")
            # stuid=request.GET.get("sid")
            # Sco=request.GET.get("sco")
            # Gain=request.GET.get("gaindata")
            astudent=Student.objects.get(sno=stuid)
            acourse=Course.objects.get(cno=couid)
            result=Achievement()
            result.course=acourse
            result.student=astudent
            result.score=Sco
            result.gain_date=Gain
            result.save()
            result=Achievement.objects.values().filter(sno=stuid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def showAchievements(request):
    '''
        http://127.0.0.1:8000/showAchievements
    '''
    result=Achievement.objects.values("score","gain_date","student_id","course_id")
    return showJsonresult(result)

def updateAchievement(request):
    '''
    http://127.0.0.1:8000/updateAchievement
    '''
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            resdata = data["data"]
            couid=resdata["cid"]
            stuid=resdata["sid"]
            Sco=resdata["sco"]
            Gain=resdata["gaindata"]
            # c1=Achievement.objects.get(score=Sco)
            # c2=Achievement.objects.get(score=Sco)
            # s1=Achievement.objects.get(gain_date=newGain)
            # s2=Achievement.objects.get(score=Gain)
            # s=Student.objects.get(sno=stuid)
            # s.studentCourse.add(c1)
            # s.studentCourse.remove(c2)
            # s.studentCourse.add(s1)
            # s.studentCourse.remove(s2)
            former=Achievement.objects.get(student_id=stuid,course_id=couid)
            former.delete()
            astudent=Student.objects.get(sno=stuid)
            acourse=Course.objects.get(cno=couid)
            result=Achievement()
            result.course=acourse
            result.student=astudent
            result.gain_date=Gain
            result.score=Sco
            result.save()
            result=Achievement.objects.values().filter(student_id=stuid)
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def delAchievement(request):
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            resdata = data["data"]
            stuid=resdata["sid"]
            couid=resdata["cid"]
            tresult=Achievement.objects.filter(student_id=stuid).filter(course_id=couid).delete()
        return showJsonresult(tresult)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)