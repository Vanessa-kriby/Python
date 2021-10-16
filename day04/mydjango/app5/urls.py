from django.urls import path 
from app5.dateview.addstudent import *
from app5.dateview.showstudent import *
from app5.dateview.updatestudent import *
from app5.dateview.delstudent import *
from app5.dateview.retriveStudent import *
from app5.dateview.retriveCourse import *
from app5.dateview.postStudentCourse import *

urlpatterns = [
    path("addStudents",addStudents,name="addStudents"),
    path("showStudents",showStudents,name="showStudents"),
    path("updateStudent",updateStudent,name="updateStudent"),
    path("delStudent",delStudent,name="delstudent"),
    path("retriveStudent",retriveStudent,name="retriveStudent"),
    path("retriveCourse",retriveCourse,name="retriveCourse"),
    path("postStudentCourse",postStudentCourse,name="postStudentCourse"),
]