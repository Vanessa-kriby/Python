from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import *
import json

def hello(request):
    return HttpResponse("Hello world!")

def addGrades(request):
    '''
        http://127.0.0.1:8000/addGrades?cname=2019计科
    '''
    response={}
    try:
        response['msg']="Success !"
        response['err_num']=0
        tgrade=Grade(cName=request.GET.get("cname"))
        tgrade.save()
        return HttpResponse(json.dumps(response),'application/json')
    except Exception as e:
        response['msg']=str(e)
        response['err_num']=1
        return HttpResponse(response)

def showGrades(request):
    '''
        curl "http://127.0.0.1:8000/showGrades"
    '''
    result=Grade.objects.all().values()
    return showJsonresult(result)
    # try:
        # tgrade=Grade.objects.all().values()
        # sgrade=serializers.serialize("json",tgrade)
        # sgrade=json.dumps(list(tgrade))
        # return HttpResponse("good luck")
        # return HttpResponse(sgrade,'application/json')
    # except Exception as e:
        # print(e)
        # return HttpResponse(e)
    # return JsonResponse(sgrade,safe=False)

def updateGrade(request):
    '''
        curl "http:127.0.0.1:8000/updateGrade?gid=4&gname=2013上戏"
    '''
    try:
        id=request.GET.get("gid")
        tname=request.GET.get("gname")
        result=Grade.objects.get(cId=id)
        result.cName=tname
        result.save()
        result=Grade.objects.values().filter(cId=id)
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response[err_num]=1
        return showJsonerror(response)

def delGrade(request):
    '''
        http://127.0.0.1:8000/delGrade?
    '''
    try:
        id=request.GET.get("gid")
        tname=request.GET.get("gname")
        tresult=Grade.objects.filter(cId=id).delete()
        return showJsonresult(tresult)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def addStudents(request):
    '''
        curl "http://127.0.0.1:8000/addStudents?stid=2020&stname=刘昊然&stgender=boy&tclassid=1"
    '''
    response={}
    try:
        response['msg']="Success !"
        response['err_num']=0
        tid=request.GET.get("stid")
        tname=request.GET.get("stname")
        tgender=request.GET.get("stgender")
        tcid=request.GET.get("tclassid")
        print(' %s %s %s %s' % (tid,tname,tgender,tcid))
        tGrade=Grade.objects.get(cId=tcid)
        print(tGrade)
        tgrade=Student(sno=tid,sname=tname,sgender=tgender,sclass=tGrade)
        tgrade.save()
        return HttpResponse(json.dumps(response),'application/json')
    except Exception as e:
        response['msg']=str(e)
        response['err_num']=1
        return HttpResponse(response)

def showStudents(request):
    '''
        curl "http://127.0.0.1:8000/showStudents"
    '''
    result=Student.objects.values("sno","sname","sgender")
    return showJsonresult(result)
    # try:
        # students=Student.objects.values("sno","sname","sgender")
        # stu=json.dumps(list(students))
        # return HttpResponse(stu,'application/json')
    # except Exception as e:
        # print(e)
        # return HttpResponse(e)

def updateStudent(request):
    '''
        curl "http:127.0.0.1:8000/updateStudent"
    '''

def delStudent(request):
    '''
        http://127.0.0.1:8000/delStudent?stid=xx
    '''
    try:
        id=request.GET.get("stid")
        tresult=Student.objects.filter(sno=id).delete()
        return showJsonresult(tresult)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def addCourses(request):
    '''
        curl "http://127.0.0.1:8000/addCourses?cid=1&cname=example"
    '''
    response={}
    try:
        response['msg']="good job!"
        response['err_num']=0
        cid=request.GET.get("cid")
        cname=request.GET.get("cname")
        print(' %s %s ' % (cid,cname))
        tCourses=Courses(Ccode=cid,Cname=cname)
        tCourses.save()
        return HttpResponse(json.dumps(response),'application/json')
    except Exception as e:
        response['msg']=str(e)
        response['err_num']=1
        return HttpResponse(response)

def showCourses(request):
    '''
        curl "http://127.0.0.1:8000/showCourses"
    '''
    result=Courses.objects.all().values()
    return showJsonresult(result)
    # try:
        # cid=Courses.objects.all().values()
        # scid=serializers.serialize("json",cid)
        # scid=json.dumps(list(cid))
        # cname=Courses.objects.all()
        # scname=serializers.serialize("json",scname)
        # return HttpResponse(scid,'application/json')
    # except Exception as e:
        # print(e)
        # return HttpResponse(e)

def updateCourse(request):
    '''
        curl "http://127.0.0.1:8000/updateCourse"
    '''

def delCourse(request):
    '''
        http://127.0.0.1:8000/delCourse?
    '''
    try:
        id=request.GET.get("couno")
        c1=Courses.objects.get(Ccode=id)
        c1.student_set.clear()
        tresult=Courses.objects.filter(Ccode=id).delete()
        return showJsonresult(tresult)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return showJsonerror(response)

def selectCourses(request):
    '''
        curl "http://127.0.0.1:8000/selectCourses?sno=006&cno=7"
    '''
    response={}
    try:
        response['msg']="Good luck"
        response['err_num']=0
        stuID=request.GET.get("sno")
        couID=request.GET.get("cno")
        s=Student.objects.get(sno=stuID)
        c=Courses.objects.get(Ccode=couID)
        s.scourses.add(c)
        # return HttpResponse("good luck")
        # return HttpResponse(json.dumps(list(s.scourses.add(c))),'application/json')
        return HttpResponse(json.dumps(response),'application/json')
    except Exception as e:
        # print(e)
        # return HttpResponse(e)
        response['msg']=str(e)
        response['err_num']=1
        return HttpResponse(response)

def forwardShowSelectCourses(request):           #正向查询
    '''
        curl "http://127.0.0.1:8000/forwardShowSelectCourses"
    '''
    result=Student.objects.all().values("sno","sname","sgender","sclass__cName","scourses__Cname")
    return showJsonresult(result)
    # try:
        # students=Student.objects.values("sno","sname","sgender","sclass__cName","scourses__Cname")
        # stu=json.dumps(list(students))
        # return HttpResponse(stu,'application/json')
    # except Exception as e:
        # print(e)
        # return HttpResponse(e)

def reverseShowSelectCourses(request):       #反向查询
    '''
        curl "http://127.0.0.1:8000/reverseShowSelectCourses"
    '''
    result=Courses.objects.filter(student__sname='邓紫棋').values("Ccode","Cname")
    return showJsonresult(result)
    # try:
        # cour=Courses.objects.filter(student__sname='邓紫棋').values("Ccode","Cname")
        # print(cour)
        # cours=json.dumps(list(cour))
        # return HttpResponse("G.E.M")
        # return HttpResponse(cours,'application/json')
    # except Exception as e:
        # print(e)
        # return HttpResponse(e)

def unShowSelectCourses(request):
    '''
        curl "http://127.0.0.1:8000/unShowSelectCourses"
    '''
    result=Student.objects.filter(scourses__Cname__isnull=True).values("sno","sname","sclass__cName")
    return showJsonresult(result)
    # try:
        # stud=Student.objects.filter(scourses__Cname__isnull=True).values("sno","sname","sclass__cName")
        # stude=json.dumps(list(stud))
        # return HttpResponse(stude,'application/json')
    # except Exception as e:
        # print(e)
        # return HttpResponse(e)

def displayStudentCourses(request):
    '''
        curl "http://127.0.0.1:8000/displayStudentCourses"
    '''
    result=Student.objects.filter(scourses__Cname__isnull=False).values("sno","sname","sgender","sclass__cName","scourses__Cname")
    return showJsonresult(result)
    # try:
        # studen=Student.objects.filter(scourses__Cname__isnull=False).values("sno","sname","sgender","sclass__cName","scourses__Cname")
        # student=json.dumps(list(studen))
        # return HttpResponse(student,'application/json')
    # except Exception as e:
        # print(e)
        # return HttpResponse(e)

def updateSelectCourse(request):
    '''
        curl "http://127.0.0.1:8000/updateSelectCourse?"
    '''
    try:
        stuID=request.GET.get("sno")
        couID=request.GET.get("cno")
        newcouID=request.GET.get("newcno")
        c2=Courses.objects.get(Ccode=newcouID)
        c1=Courses.objects.get(Ccode=couID)
        s=Student.objects.get(sno=stuID)
        # c1.student_set.remove(s)
        # c2.student_set.add(s)
        s.scourses.add(c2)
        s.scourses.remove(c1)
        result=Student.objects.filter(scourses__Ccode=newcouID).filter(sno=stuID).values()
        return showJsonresult(result)
    except Exception as e:
        response={}
        response['msg']=str(e)
        response['err_num']=1
        return  showJsonerror(response)
def delSelectCourse(request):
    

def showJsonresult(result):
    '''
        curl "http://127.0.0.1:8000/showJsonresult"
    '''
    response={}
    try:
        response['msg']="good job!"
        response['err_num']=0
        response['data']=list(result)
        return HttpResponse(json.dumps(response),'application/json')
    except Exception as e:
        response['msg']=str(e)
        response['err_num']=1
        return HttpResponse(response)

def showJsonerror(result):
    return HttpResponse(json.dumps(response),'application/json')

    #update和del部分未完善，且都未经过测试，测试将在代码完善后统一测试