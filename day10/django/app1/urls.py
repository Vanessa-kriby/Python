from django.urls import path
from app1.dateview.addDepartments import *
from app1.dateview.showDepartments import *
from app1.dateview.updateDepartment import *
from app1.dateview.delDepartment import *

urlpatterns =[
    path("addDepartments",addDepartments,name="addDepartments"),
    path("showDepartments",showDepartments,name="showDepartments"),
    path("updateDepartment",updateDepartment,name="updateDepartment"),
    path("delDepartment",delDepartment,name="delDepartment"),
]