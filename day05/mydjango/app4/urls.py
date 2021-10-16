from django.urls import path
from app4.views import *
from app4.dateview.addTeachPlans import *
from app4.dateview.showTeachPlans import *
from app4.dateview.delTeachPlan import *
from app4.dateview.updateTeachPlan import *



urlpatterns =[


    path("addTeachPlans", addTeachPlans, name="addTeachPlans"),
    path("showTeachPlans", showTeachPlans, name="showTeachPlans"),
    path("delTeachPlan", delTeachPlan, name="delTeachPlan"),
    path("updateTeachPlan", updateTeachPlan, name="updateTeachPlan"),


]