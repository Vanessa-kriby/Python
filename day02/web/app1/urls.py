from django.urls import path 
from app1.data.student import *
from app1.data.course import *
from app1.data.achievement import *
from app1.data.grade import *
from app1.data.teacher import *
from app1.data.teachplan import *


urlpatterns = [
    path("addStudents",addStudents,name="addStudents"),
    path("showStudents",showStudents,name="showStudents"),
    path("updateStudent",updateStudent,name="updateStudent"),
    path("delStudent",delStudent,name="delstudent"),
    path("showAchievements",showAchievements,name="showAchievements"),
    path('addGrades',addGrades,name="addGrades"),
    path('showGrades',showGrades,name="showGrades"),
    path("updateGrade",updateGrade,name="updateGrade"),
    path("delGrade",delGrade,name="delGrade"),
    path("addCourses",addCourses,name="addCourses"),
    path("showCourses",showCourses,name="showCourses"),
    path("updateCourse",updateCourse,name="updateCourse"),
    path("delCourse",delCourse,name="delCourse"),
    path("addTeachPlans",addTeachPlans,name="addTeachPlans"),
    path("showTeachPlans",showTeachPlans,name="showTeachPlans"),
    path("updateTeachPlan",updateTeachPlan,name="updateTeachPlan"),
    path("delTeachPlan",delTeachPlan,name="delTeachPlan"),
    path("addTeachers",addTeachers,name="addTeachers"),
    path("showTeachers",showTeachers,name="showTeachers"),
    # path("updateTeacher",updateTeacher,name="updateTeacher"),
    path("delTeacher",delTeacher,name="delteacher"),
    path("addAchievements",addAchievements,name="addAchievements"),
    path("showAchievements",showAchievements,name="showAchievements"),
    path("updateAchievement",updateAchievement,name="updateAchievement"),
    path("delAchievement",delAchievement,name="delAchievement"),
]