from django.urls import path
from app6.dateview.showachievement import *
from app6.dateview.addachievement import *
from app6.dateview.delachievement import *
from app6.dateview.updateachievement import *

urlpatterns = [
    path('addAchievements',addAchievements,name='addAchievements'),
    path('showAchievements',showAchievements,name='showAchievements'),
    path('updateAchievement',updateAchievement,name='updateAchievement'),
    path('delAchievement',delAchievement,name='delAchievement'),
]