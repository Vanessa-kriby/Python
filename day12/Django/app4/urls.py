from django.urls import path
from app4.dateview.addCourses import *
from app4.dateview.showCourses import *
from app4.dateview.updateCourse import *
from app4.dateview.delCourse import *

urlpatterns =[
    path("addCourses",addCourses,name="addCourses"),
    path("showCourses",showCourses,name="showCourses"),
    path("updateCourse",updateCourse,name="updateCourse"),
    path("delCourse",delCourse,name="delCourse"),
]