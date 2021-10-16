from django.urls import path
from app7.dateview.addTeachings import *
from app7.dateview.displayTeachings import *
from app7.dateview.delTeaching import *
from app7.dateview.updateTeaching import *
from app7.dateview.showTeachings import *

urlpatterns =[
    path('addTeachings',addTeachings,name='addTeachings'),
    path('displayTeachings',displayTeachings,name='displayTeachings'),
    path('delTeaching',delTeaching,name='delTeaching'),
    path('updateTeaching',updateTeaching,name='updateTeaching'),
    path('showTeachings',showTeachings,name='showTeachings'),
]