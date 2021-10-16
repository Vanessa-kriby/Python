from django.urls import path
from app6.dateview.addStudents import *
from app6.dateview.showStudents import *
from app6.dateview.delStudent import *
from app6.dateview.updateStudent import *
from app6.dateview.displayStudents import *

urlpatterns =[
    path("addStudents",addStudents,name="addStudents"),
    path("showStudents",showStudents,name="showStudents"),
    path("delStudent",delStudent,name="delStudent"),
    path("updateStudent",updateStudent,name="updateStudent"),
    path("displayStudents",displayStudents,name="displayStudents"),
    
]