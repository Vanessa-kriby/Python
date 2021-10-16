from django.urls import path
from app3.dateview.addTeachers import *
from app3.dateview.showTeachers import *
from app3.dateview.updateTeacher import *
from app3.dateview.delTeacher import *
from app3.dateview.retrieveTeacher import *
from app3.dateview.teachCourse import *

urlpatterns =[
    path("addTeachers",addTeachers,name="addTeachers"),
    path("showTeachers",showTeachers,name="showTeachers"),
    path("updateTeacher",updateTeacher,name="updateTeacher"),
    path("delTeacher",delTeacher,name="delTeacher"),
    path("retrieveTeacher",retrieveTeacher,name="retrieveTeacher"),
    path("teachCourse",teachCourse,name="teachCourse"),
]