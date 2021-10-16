from django.urls import path
from app1.dateview.addTeachPlans import *
from app1.dateview.showTeachPlans import *
from app1.dateview.updateTeachPlan import *
from app1.dateview.delTeachPlan import *

urlpatterns =[
    path("addTeachPlans",addTeachPlans,name="addTeachPlans"),
    path("showTeachPlans",showTeachPlans,name="showTeachPlans"),
    path("updateTeachPlan",updateTeachPlan,name="updateTeachPlan"),
    path("delTeachPlan",delTeachPlan,name="delTeachPlan"),
]