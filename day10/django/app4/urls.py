from django.urls import path
from app4.dateview.addTeachPlans import *
from app4.dateview.showTeachPlans import *
from app4.dateview.updateTeachPlan import *
from app4.dateview.delTeachPlan import *

urlpatterns =[
    path("addTeachPlans",addTeachPlans,name="addTeachPlans"),
    path("showTeachPlans",showTeachPlans,name="showTeachPlans"),
    path("updateTeachPlan",updateTeachPlan,name="updateTeachPlan"),
    path("delTeachPlan",delTeachPlan,name="delTeachPlan"),
]