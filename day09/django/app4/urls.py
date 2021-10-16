from django.urls import path
from app4.dateview.addTeachers import *
from app4.dateview.delTeacher import *
from app4.dateview.showTeachers import *
from app4.dateview.retriveTeacher import *
from app4.dateview.getteachCourse import *
from app4.dateview.updateTeacher import *
from app4.dateview.retriveTeachPlan import *

urlpatterns =[
    path('addTeachers',addTeachers,name='addTeachers'),
    path('delTeacher',delTeacher,name='delTeacher'),
    path('showTeachers',showTeachers,name='showTeachers'),
    path('retriveTeacher',retriveTeacher,name='retriveTeacher'),
    path('getteachCourse',getteachCourse,name='getteachCourse'),
    path('updateTeacher',updateTeacher,name='updateTeacher'),
    path('retriveTeachPlan',retriveTeachPlan,name='retriveTeachPlan'),
]