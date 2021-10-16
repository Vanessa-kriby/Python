from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.CharField(max_length=20,primary_key=True)
    sname=models.CharField(max_length=50)
    sgender=models.CharField(max_length=10)
    sclass=models.ForeignKey("Grade",on_delete=models.CASCADE)
    scourses = models.ManyToManyField("Courses")

class Grade(models.Model):
    cId=models.AutoField(primary_key=True)
    cName=models.CharField(max_length=100)
    def __str__(self):
        return self.cName
class Courses(models.Model):
    Ccode=models.CharField(max_length=50,primary_key=True)
    Cname=models.CharField(max_length=100)
    
    def __str__(self):
        return super().__str__()
