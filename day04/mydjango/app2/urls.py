from django.urls import path
from app2.dateview.addcourse import *
from app2.dateview.showcourse import *
from app2.dateview.delcourse import *
from app2.dateview.delcourse import *
from app2.dateview.updatecourse import *



urlpatterns =[
    path("addCourses",addCourses,name="addCourses"),
    path("showCourses",showCourses,name="showCourses"),
    path("delCourse",delCourse,name="delCourse"),
    path("updateCourse",updateCourse,name="updateCourse"),
]