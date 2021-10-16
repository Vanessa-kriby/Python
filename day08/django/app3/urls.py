from django.urls import path
from app3.dateview.addCourses import *
from app3.dateview.showCourses import *
from app3.dateview.updateCourse import *
from app3.dateview.delCourse import *

urlpatterns =[
    path("addCourses",addCourses,name="addCourses"),
    path("showCourses",showCourses,name="showCourses"),
    path("updateCourse",updateCourse,name="updateCourse"),
    path("delCourse",delCourse,name="delCourse"),
]