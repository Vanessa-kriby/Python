from django.urls import path
from app7.dateview.addPointsScoring import *
from app7.dateview.showPointsScoring import *
from app7.dateview.updatePointsScoring import *

urlpatterns =[
    path("addPointsScoring",addPointsScoring,name="addPointsScoring"),
    path("showPointsScoring",showPointsScoring,name="showPointsScoring"),
    path("updatePointsScoring",updatePointsScoring,name="updatePointsScoring"),
]