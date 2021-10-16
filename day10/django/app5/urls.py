from django.urls import path
from app5.dateview.addStudents import *
from app5.dateview.showStudents import *
from app5.dateview.updateStudent import *
from app5.dateview.delStudent import *
from app5.dateview.retriveStudent import *
from app5.dateview.postStudentCourse import *
from app5.dateview.showStudentCourse import *
from app5.dateview.delStudentCourse import *

urlpatterns =[
    path("addStudents",addStudents,name="addStudents"),
    path("showStudents",showStudents,name="showStudents"),
    path("updateStudent",updateStudent,name="updateStudent"),
    path("delStudent",delStudent,name="delStudent"),
    path("retriveStudent",retriveStudent,name="retriveStudent"),
    path("postStudentCourse",postStudentCourse,name="postStudentCourse"),
    path("showStudentCourse",showStudentCourse,name="showStudentCourse"),
    path("delStudentCourse",delStudentCourse,name="delStudentCourse"),
]