from django.urls import path
from app1.dateview.addConsequences import *
from app1.dateview.showConsequences import *
from app1.dateview.displayConsequences import *
from app1.dateview.updateConsequence import *
from app1.dateview.delConsequence import *

urlpatterns =[
    path("addConsequences",addConsequences,name="addConsequences"),
    path("showConsequences",showConsequences,name="showConsequences"),
    path("displayConsequences",displayConsequences,name="displayConsequences"),
    path("updateConsequence",updateConsequence,name="updateConsequence"),
    path("delConsequence",delConsequence,name="delConsequence"),
]