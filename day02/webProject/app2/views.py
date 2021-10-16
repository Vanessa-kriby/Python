from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import *
import json
import datetime

def hello(request):
    return HttpResponse("Hello world!")

def addGrades(request):
    '''
        http://127.0.0.1:8000/addGrades?cid=1&cname=2019计科
    '''
    try:
        request.GET.get=request.GET.get("request.GET.get")
        request.GET.get_d=json.loads(request.GET.get)
        
        id=request.GET.get_d['cid']
        tname=request.GET.get_d['cname']
        # id=request.GET.get("cid")
        # tname=request.GET.get("cname")
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

def updateGrade(request):
    '''
        http://127.0.0.1:8000/updateGrade?gid=2&gname=2020计科
    '''
    try:
        request.GET.get=request.GET.get("request.GET.get")
        request.GET.get_d=json.loads(request.GET.get)

        id=request.GET.get_d['gid']
        tname=request.GET.get_d['gname']
        # id=request.GET.get("gid")
        # tname=request.GET.get("gname")
        result=Grade.objects.get(gno=id)
        result.gname=tname
        result.save()
        result=Grade.objects.values().filter(gno=id)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def delGrade(request):
    '''
        http://127.0.0.1:8000/delGrade?gid=xx
    '''
    try:
        request.GET.get=request.GET.get("request.GET.get")
        request.GET.get_d=json.loads(request.GET.get)

        id=request.GET.get_d['gid']
        # id=request.GET.get("gid")
        tresult=Grade.objects.filter(gno=id).delete()
        return showJsonresult(tresult)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def addCourses(request):
    '''
        http://127.0.0.1:8000/addCourses?couid=1314&couname=生物&coubook=生物2
    '''
    try:
        cid=request.GET.get("couid")
        cName=request.GET.get("couname")
        cbook=request.GET.get("coubook")
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
    result=Course.objects.all().values()
    return showJsonresult(result)

def updateCourse(request):
    '''
        http://127.0.0.1:8000/updateCourse?couid=1&couname=C&coubook=xxx
    '''
    try:
        cid=request.GET.get("couid")
        cName=request.GET.get("couname")
        cbook=request.GET.get("coubook")
        result=Course.objects.get(cno=cid)
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
    
def delCourse(request):
    '''
        http://127.0.0.1:8000/delCourse?couid=xx
    '''
    try:
        id=request.GET.get("couid")
        c1=Course.objects.get(cno=id)
        c2=student_set.clear()     
        tresult=Course.objects.filter(cno=id).delete()
        return showJsonresult(tresult)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def addTeachPlans(request):
    '''
        http://127.0.0.1:8000/addTeachPlans?cid=1314&gra=2&cri=3.0&teadate=2019-9-1&Checktype=考试
    '''
    try:
        co=request.GET.get("cid")
        gr=request.GET.get("gra")
        cr=request.GET.get("cri")
        tedate=request.GET.get("teadate")
        checktype=request.GET.get("Checktype")
        tCourse=Course.objects.get(cno=co)
        tGrade=Grade.objects.get(gno=gr)
        tPlant=TeachPlan()
        tPlant.course=tCourse
        tPlant.grade=tGrade
        tPlant.credit=cr
        tPlant.teach_date=tedate
        tPlant.checkType=checktype
        tPlant.save()
        result=TeachPlan.objects.all().values("credit","teach_date","checkType")
        # tedate=json.dumps(list(result),cls=CJsonEncoder)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def showTeachPlans(request):
    '''
        http://127.0.0.1:8000/showTeachPlans
    '''
    result=TeachPlan.objects.all().values()
    return showJsonresult(result)

def updateTeachPlan(request):
    '''
        http://127.0.0.1:8000/updateTeachPlan?cid=1314&gra=2&cri=3.0&teadate=2019-9-1&Checktype=考试
    '''
    try:
        co=request.GET.get("cid")
        gr=request.GET.get("gra")
        cr=request.GET.get("cri")
        tedate=request.GET.get("teadate")
        checktype=request.GET.get("Checktype")
        tCourse=Course.objects.get(cno=co)
        tGrade=Grade.objects.get(gno=gr)
        result=TeachPlan(course=tCourse,grade=tGrade,credit=cr,teach_date=tedate,checkType=checktype)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
def delTeachPlan(request):
    '''
        http://127.0.0.1:8000/delTeachPlan?cid=1314&gra=2
    '''
    try:
        co=request.GET.get("cid")
        gr=request.GET.get("gra")
        tCourse=Course.objects.get(cno=co)
        tGrade=Grade.objects.get(gno=gr)
        result=Course.objects.filter(cno=co).delete()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def addTeachers(request):
    '''
     http://127.0.0.1:8000/addTeachers?teid=xx&teName=xx&teGender=xx&tejobTitle=xx
    '''
    try:
        tid=request.GET.get("teid")
        tName=request.GET.get("teName")
        tGender=request.GET.get("teGender")
        tjobTitle=request.GET.get("tejobTitle")
        result=Teacher(tno=tid,tname=tName,gender=tGender,jobTitle=tjobTitle)
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

def updateTeacher(request):
    '''
        http://127.0.0.1:8000/updateTeacher?teid=1&teName=xx&teGender=女&tejobTitle=xx
    '''
    try:
        tid=request.GET.get("teid")
        tName=request.GET.get("teName")
        tGender=request.GET.get("teGender")
        tjobTitle=request.GET.get("tejobTitle")
        tresult=Teacher.objects.get(tno=tid)
        tresult.tname=tName
        tresult.gender=tGender
        tresult.jobTitle=tjobTitle
        tresult.save()
        tresult=Teacher.objects.values().filter(tno=tid)
        return showJsonresult(tresult)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def delTeacher(request):
    '''
        http://127.0.0.1:8000/delTeacher?teid=1
    '''
    try:
        tid=request.GET.get("teid")
        tresult=Teacher.objects.filter(tno=tid).delete()
        return showJsonresult(tresult)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def addTeachings(request):
    '''
        http://127.0.0.1:8000/addTeachings?tid=xx&cid=xx
    '''
    try:
        tID=request.GET.get("tid")
        cID=request.GET.get("cid")
        t=Teacher.objects.get(tno=tID)
        c=Course.objects.get(cno=cID)
        t.teachCourse.add(c)
        result=Course.objects.values('cno','cname').filter(cno=cID)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def showTeachings(request):
    '''
        http://127.0.0.1:8000/showTeachings
    '''
    result=Course.objects.filter(teacher__tname="").values("","")
    return showJsonresult(result)
    
def updateTeaching(request):
    '''
        http://127.0.0.1:8000/updateTeaching?tid=xx&cid=1&newcid=xx
    '''
    try:
        tID=request.GET.get("tid")
        cID=request.GET.get("cid")
        newcID=request.GET.get("newcid")
        c2=Course.objects.get(cno=newcID)
        c1=Course.objects.get(cno=cID)
        t=Teacher.objects.get(tno=tID)
        t.teachCourse.add(c2)
        t.teachCourse.remove(c1)
        result=Teacher.objects.filter(teachCourse__cno=newcID).filter(tno=tID).values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def delTeaching(request):
    '''
        http://127.0.0.1:8000/delTeaching?tid=520&cid=1314
    '''
    try:
        tID=request.GET.get("tid")
        cID=request.GET.get("cid")
        c1=Course.objects.get(cno=cID)
        t=Teacher.objects.get(tno=tID)
        t.teachCourse.remove(c1)
        return showJsonresult('request.GET.get:""')
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def addStudents(request):
    '''
        http://127.0.0.1:8000/addStudents?sid=001&stName=邓紫棋&stGender=女
    '''
    try:
        sID=request.GET.get("sid")
        sName=request.GET.get("stName")
        sGender=request.GET.get("stGender")
        result=Student(sno=sID,sname=sName,gender=sGender)
        result.save()
        result=Student.objects.values().filter(sno=sID)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def addStudentCourse(request):
    '''
        http://127.0.0.1:8000/addStudentCourse?sid=001&cid=1314
    '''
    try:
        tID=request.GET.get("sid")
        cID=request.GET.get("cid")
        s=Student.objects.get(sno=tID)
        c=Course.objects.get(cno=cID)
        tachievement=Achievement()
        tachievement.course=c
        tachievement.student=s
        tachievement.score=0.0
        tachievement.gain_date="2020-9-2"
        tachievement.save()
        # s.studentCourse.add(c)
        # 通过achievement 自动添加到student
        result=Student.objects.values().filter(sno=tID)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)
   
def showStudents(request):
    '''
        http://127.0.0.1:8000/showStudents?isNull=1
        0 True
        1 False
    '''
    tnull=request.GET.get("isNull")
    t=True
    if(tnull=='1'):
        t=False
    result=Student.objects.filter(achievement__isnull=t).values("sno","sname","gender","studentCourse","achievement")
    return showJsonresult(result)

def updateStudent(request):
    '''
        http://127.0.0.1:8000/updateStudent?sid=001&stName=林允儿&stGender=女
    '''
    try:
        sID=request.GET.get("sid")
        sName=request.GET.get("stName")
        sGender=request.GET.get("stGender")
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
        sid=request.GET.get("stid")
        result=Student.objects.filter(sno=sid).delete()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def addAchievements(request):
    '''
        http://127.0.0.1:8000/addAchievements?cou=1314&stu=001&scr=1.0&gainDate=2013-1-4
    '''
    try:
         if(request.method=='POST'):
            data = json.loads(request.body)
            data = data["data"]

            co=data("cou")
            st=data("stu")
            sc=data("scr")
            gaindate=data("gainDate")
            acourse=Course.objects.get(cno=co)
            astudent=Student.objects.get(sno=st)
            achieve=Achievement()
            achieve.course=acourse
            achieve.student=astudent
            achieve.score=sc
            achieve.gain_date=gaindate
            achieve.save()
            result=Achievement.objects.all().values()
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
    result=Achievement.objects.all().values()
    return showJsonresult(result)

def updateAchievement(request):
    '''
        http://127.0.0.1:8000/updateAchievement?cou=&stu=&scr=&gainDate=
    '''
    try:
        co=request.GET.get("cou")
        st=request.GET.get("stu")
        sc=request.GET.get("scr")
        gaindate=request.GET.get("gainDate")
        acourse=Course.objects.get(cno=co)
        astudent=Student.objects.get(sno=st)
        result=Achievement(course=acourse,student=astudent,score=sc,gain_date=gaindate)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def delAchievement(request):
    '''
        http://127.0.0.1:8000/delAchievement?cou=1314&stu=001
    '''

    try:
        co=request.GET.get("cou")
        st=request.GET.get("stu")
        acourse=Course.objects.get(cno=co)
        astudent=Student.objects.get(sno=st)
        result=Course.objects.filter(cno=co).delete()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def showJsonresult(result):
    response={}
    try:
        response['msg']="good job!"
        response['err_num']=0
        response['data']=list(result)
        return HttpResponse(json.dumps(response,cls=CJsonEncoder),'application/json')
    except Exception as e:
        response['msg']=str(e)
        response['err_num']=1
        return HttpResponse(response)

def showJsonerror(response):
    return HttpResponse(json.dumps(response),'application/json')

class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            # 这里可以统一修改想要的格式
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            # 这里可以统一修改想要的格式
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)  
