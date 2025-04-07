from django.db import models

class SixStudentID(models.Model):
    name = models.CharField(max_length=20)
    FatherName = models.CharField(max_length=20)
    MotherName =  models.CharField(max_length=20)
    roll = models.IntegerField(max_length=5)
    StudentID = models.IntegerField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.StudentID)
    
class ClassSixTeachers(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    NID = models.IntegerField(max_length=17)
    password = models.CharField(max_length=18)

    def __str__(self):
        return self.name
    
class ClassSIXResult(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(max_length=5)
    student_id = models.IntegerField(max_length=10)
    FatherName = models.CharField(max_length=20)

    bangla = models.FloatField(max_length=5)
    english = models.FloatField(max_length=5)
    math = models.FloatField(max_length=5)
    biology = models.FloatField(max_length=5)
    chemistry = models.FloatField(max_length=5)
    physics = models.FloatField(max_length=5)

    total = models.FloatField(max_length=10)
    avarage = models.FloatField(max_length=5)

    def __str__(self):
        return self.student_id
    

# Create your models here.