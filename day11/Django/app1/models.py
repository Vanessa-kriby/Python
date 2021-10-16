from django.db import models

# Create your models here.
class Department(models.Model):
    dno=models.CharField(max_length=20,primary_key=True)
    dname=models.CharField(max_length=50,unique=True)
    class Meta():
        db_table = "department"

class Classroom(models.Model):
    crno=models.CharField(max_length=20,primary_key=True)
    seat=models.CharField(max_length=20)
    kind=models.CharField(max_length=20)
    class Meta():
        db_table= "classroom"


class Course(models.Model):
    cno=models.CharField(max_length=20,primary_key=True)
    cname=models.CharField(max_length=50)
    textBook=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    classroom=models.ForeignKey("Classroom", on_delete=models.CASCADE)
    departmentCourse=models.ManyToManyField("Department",through="TeachPlan")
    class Meta():
        db_table = "course"

class Teacher(models.Model):
    tno=models.CharField(max_length=20,primary_key=True)
    tname=models.CharField(max_length=50)
    tgender=models.CharField(max_length=20)
    jobtitle=models.CharField(max_length=20)
    teachCourse=models.ManyToManyField("Course",through="TeachPlan")
    class Meta():
        db_table = "teacher"