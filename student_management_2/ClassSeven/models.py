from django.db import models

class ClassSevenStudentID(models.Model):
    name = models.CharField(max_length=20)
    FatherName = models.CharField(max_length=20)
    MotherNmae = models.CharField(max_length=20)


    StudentID = models.IntegerField()
    roll = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"(self.StudentID)-self.name"
    
    
class ClassSevenResult(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    StudentID = models.IntegerField()

    bangla = models.FloatField()
    english = models.FloatField()
    math = models.FloatField()
    biology = models.FloatField()
    chemistry = models.FloatField()
    physics = models.FloatField()

    total = models.FloatField()
    avarage = models.FloatField()

    def __str__(self):
        return f"(self.StudentID)-self.name"
    
class ClassSevenTeachers(models.Model):
    name = models.CharField(max_length=20)
    NID = models.IntegerField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Create your models here.
