from django.urls import path
from app4 import views
from app4.dateview.addteacher import *
from app4.dateview.delteacher import *
from app4.dateview.showteacher import *
from app4.dateview.updateteacher import *
from app4.dateview.getTeachCourse import *
from app4.dateview.addTeachCourse import *
from app4.dateview.updateTeachCourse import *
from app4.dateview.delTeachCourse import *

urlpatterns = [
    path("addTeachers",addTeachers, name="addTeachers"),
    path("delTeacher",delTeacher, name="delTeacher"),
    path("showTeachers",showTeachers, name="showTeachers"),
    path("updateTeacher",updateTeacher, name="updateTeacher"),
    path("getTeachCourse",getTeachCourse, name="getTeachCourse"),
    path("addTeachCourse",addTeachCourse, name="addTeachCourse"),
    path('updateTeachCourse',updateTeachCourse, name='updateTeachCourse'),
    path('delTeachCourse',delTeachCourse, name='delTeachCourse'),
]