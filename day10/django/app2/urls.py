from django.urls import path
from app2.dateview.addCourses import *
from app2.dateview.showCourses import *
from app2.dateview.updateCourse import *
from app2.dateview.delCourse import *
from app2.dateview.retriveCourse import *


urlpatterns =[
    path("addCourses",addCourses,name="addCourses"),
    path("showCourses",showCourses,name="showCourses"),
    path("updateCourse",updateCourse,name="updateCourse"),
    path("delCourse",delCourse,name="delCourse"),
    path("retriveCourse",retriveCourse,name="retriveCourse"),
]