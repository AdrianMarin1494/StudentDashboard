from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    mail = models.EmailField(max_length=255, null=False)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    

class Class(models.Model):
    year = models.CharField(max_length=5, null=False)
    letter = models.CharField(max_length=1, null=False)

    def __str__(self) -> str:
        return self.year + "-" + self.letter
    

class Subject(models.Model):
    subject_name = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.subject_name
    

class Student(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name