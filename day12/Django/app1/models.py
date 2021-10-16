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
    classroom=models.ManyToManyField("Classroom", through="Advance")
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

class Advance(models.Model):
    ano=models.CharField(max_length=20,primary_key=True)
    starttime=models.TimeField()
    endtime=models.TimeField()
    week=models.CharField(max_length=20)
    teacher=models.ForeignKey("Teacher", on_delete=models.CASCADE)
    classroom=models.ForeignKey("Classroom", on_delete=models.CASCADE)
    course=models.ForeignKey("Course", on_delete=models.CASCADE)
    class Meta():
        db_table = "advance"

class TeachPlan(models.Model):
    tpno=models.CharField(max_length=20,primary_key=True)
    teach_date=models.DateField()
    evaluation_method = models.CharField(max_length=50)
    credit=models.FloatField()
    course=models.ForeignKey("Course", on_delete=models.CASCADE)
    department=models.ForeignKey("Department", on_delete=models.CASCADE)
    teacher=models.ForeignKey("Teacher", on_delete=models.CASCADE)
    class Meta():
        db_table = "teachplan"

class Student(models.Model):
    sno=models.CharField(max_length=20,primary_key=True)
    sname=models.CharField(max_length=50)
    sgender=models.CharField(max_length=20)
    studentDepartment=models.ForeignKey("Department", on_delete=models.CASCADE)
    class Meta():
        db_table = "student"

class Inventory(models.Model):
    ino=models.AutoField(primary_key=True)
    select_date=models.DateField()
    teachPlan=models.ForeignKey("TeachPlan", on_delete=models.CASCADE)
    student=models.ForeignKey("Student", on_delete=models.CASCADE)
    class Meta():
        db_table = "inventory"