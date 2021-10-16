from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from app1.models import *
import json
import datetime
from app1.comm.utils import *

def addTeachPlans(request):
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            co=data["cid"]
            gr=data["gra"]
            cr=data["cri"]
            tedate=data["teadate"]
            check=data["checktype"]
            kco=Course.objects.get(cno=co) 
            kgr=Grade.objects.get(gno=gr)
            result=TeachPlan()
            result.course=kco
            result.grade=kgr
            result.credit=cr
            result.teach_date=tedate
            result.checkType=check
            result.save()
            result=TeachPlan.objects.all().values()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def showTeachPlans(request):
    
    result=TeachPlan.objects.all().values()
    return showJsonresult(result)
    

def updateTeachPlan(request):
    try:
          if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            co=data["cid"]
            gr=data["gra"]
            cr=data["cri"]
            tedate=data["teadate"]
            check=data["checktype"]
            kk=TeachPlan.objects.filter(course=co).filter(grade=gr).delete()
            kco=Course.objects.get(cno=co)
            kgr=Grade.objects.get(gno=gr)

            result=TeachPlan()
            result.course=kco
            result.grade=kgr
            result.credit=cr
            result.teach_date=tedate
            result.checkType=check
            result.save()
            result=TeachPlan.objects.values().all()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)


def delTeachPlan(request):
    try:
        if(request.method=='POST'):
            resdata=json.loads(request.body)
            data=resdata["data"]
            co=data["cid"]
            gr=data["gra"]
            kco=Course.objects.get(cno=co)
            kgr=Grade.objects.get(gno=gr)
            result=Course.objects.filter(cno=co).delete()
            return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)   