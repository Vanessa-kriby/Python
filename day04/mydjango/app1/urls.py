from django.urls import path
from app1.dateview.addgrade import *
from app1.dateview.showgrade import *
from app1.dateview.delgrade import *
from app1.dateview.updategrade import *


urlpatterns =[
    
    path("addGrades",addGrades,name="addGrades"),
    path("showGrades",showGrades,name="showGrades"),
    path("delGrade",delGrade,name="delGrade"),
    path("updateGrade",updateGrade,name="updateGrade")
]