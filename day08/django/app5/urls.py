from django.urls import path
from app5.dateview.addStudents import *
from app5.dateview.showStudents import *
from app5.dateview.delStudent import *
from app5.dateview.retriveStudents import *
from app5.dateview.retriveCourses import *
from app5.dateview.selectStudentCourse import *
from app5.dateview.updateStudent import *


urlpatterns =[
    path('addStudents',addStudents,name='addStudents'),
    path('showStudents',showStudents,name='showStudents'),
    path('delStudent',delStudent,name='delStudent'),
    path('retriveStudents',retriveStudents,name='retriveStudents'),
    path('retriveCourses',retriveCourses,name='retriveCourses'),
    path('selectStudentCourse',selectStudentCourse,name='selectStudentCourse'),
    path('updateStudent',updateStudent,name='updateStudent'),
]