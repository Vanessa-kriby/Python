from django.urls import path
from . import views
#从当前目录导入包
urlpatterns = [
    path('', views.hello,name="hello"),
    path('addGrades',views.addGrades,name="addGrades"),
    path("showGrades",views.showGrades,name="showGrades"),
    path('updateGrade',views.updateGrade,name="updateGrade"),
    path("delGrade",views.delGrade,name="delGrade"),
    path("addStudents",views.addStudents,name="addStudents"),
    path("showStudents",views.showStudents,name="showStudents"),
    path('updateStudent',views.updateStudent,name="updateStudent"),
    path("delStudent",views.delStudent,name="delStudent"),
    path("addCourses",views.addCourses,name="addCourses"),
    path("showCourses",views.showCourses,name="showCourses"),
    path("updateCourse",views.updateCourse,name="updateCourse"),
    path("delCourse",views.delCourse,name="delCourse"),
    path("selectCourses",views.selectCourses,name="selectCourses"),
    path("forwardShowSelectCourses",views.forwardShowSelectCourses,name="forwardShowSelectCourses"),
    path("reverseShowSelectCourses",views.reverseShowSelectCourses,name="reverseShowSelectCourses"),
    path("unShowSelectCourses",views.unShowSelectCourses,name="unShowSelectCourses"),
    path('displayStudentCourses',views.displayStudentCourses,name="displayStudentCourses"),
    path("updateSelectCourse",views.updateSelectCourse,name="updateSelectCourse"),
    path("delSelectCourse",views.delSelectCourse,name="delSelectCourse"),
    path("showJsonresult",views.showJsonresult,name="showJsonresult"),
]