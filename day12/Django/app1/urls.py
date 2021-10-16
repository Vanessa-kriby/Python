from django.urls import path
from app1.dateview.addAdvance import *
from app1.dateview.showAdvance import *
from app1.dateview.updateAdvance import *
from app1.dateview.delAdvance import *

urlpatterns = [
    path("addAdvance",addAdvance,name="addAdvance"),
    path("showAdvance",showAdvance,name="showAdvance"),
    path("updateAdvance",updateAdvance,name="updateAdvance"),
    path("delAdvance",delAdvance,name="delAdvance"),
]