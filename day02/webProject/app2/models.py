from django.db import models


# Create your models here.
class Grade(models.Model):
    gno=models.CharField(max_length=20,primary_key=True)
    gname=models.CharField(max_length=20,unique=True)
    class Meta():
        db_table = 'grade'

class Course(models.Model):
    cno=models.CharField(max_length=20,primary_key=True)
    cname=models.CharField(max_length=100)
    textBook=models.CharField(max_length=50)
    gradeCourses=models.ManyToManyField("Grade",through="TeachPlan")
    class Meta():
        db_table = 'course'

class TeachPlan(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    grade = models.ForeignKey("Grade", on_delete=models.CASCADE)
    credit=models.FloatField()
    teach_date = models.DateField()
    checkType = models.CharField(max_length=50)
    class Meta():
        db_table = 'teachplan'

class Teacher(models.Model):
    tno=models.CharField(max_length=20,primary_key=True)
    tname=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    jobTitle=models.CharField(max_length=10)
    teachCourse=models.ManyToManyField("Course")
    class Meta():
        db_table = 'teacher'

class Student(models.Model):
    sno=models.CharField(max_length=50,primary_key=True)
    sname=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    studentCourse=models.ManyToManyField("Course",through='Achievement')
    class Meta():
        db_table = 'student'

class Achievement(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    score = models.FloatField()
    gain_date = models.DateField()
    class Meta():
        db_table = 'achievement'