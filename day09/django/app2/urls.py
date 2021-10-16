from django.urls import path
from app2.dateview.addDepartments import *
from app2.dateview.showDepartments import *
from app2.dateview.updateDepartment import *
from app2.dateview.delDepartment import *

urlpatterns =[
    path("addDepartments",addDepartments,name="addDepartments"),
    path("showDepartments",showDepartments,name="showDepartments"),
    path("updateDepartment",updateDepartment,name="updateDepartment"),
    path("delDepartment",delDepartment,name="delDepartment"),
]