from django.urls import path
from app5.dateview.addTeachers import *
from app5.dateview.showTeachers import *
from app5.dateview.delTeacher import *
from app5.dateview.updateTeacher import *
from app5.dateview.displayTeachers import *

urlpatterns =[
    path("addTeachers",addTeachers,name="addTeachers"),
    path("showTeachers",showTeachers,name="showTeachers"),
    path("delTeacher",delTeacher,name="delTeacher"),
    path("updateTeacher",updateTeacher,name="updateTeacher"),
    path("displayTeachers",displayTeachers,name="displayTeachers"),
    
]