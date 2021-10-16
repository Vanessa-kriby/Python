from django.urls import path
from . import views
from app3.dateview.addteachplan import *
from app3.dateview.showteachplan import *
from app3.dateview.updateteachplan import *
from app3.dateview.delteachplan import *

urlpatterns = [
    path("addTeachPlans",addTeachPlans,name="addTeachPlans"),
    path("showTeachPlans",showTeachPlans,name="showTeachPlans"),
    path("updateTeachPlan",updateTeachPlan,name="updateTeachPlan"),
    path("delTeachPlan",delTeachPlan,name="delTeachPlan"),
]