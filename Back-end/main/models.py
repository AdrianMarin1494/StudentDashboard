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
        return f"{self.first_name} {self.last_name}"
    

class ClassAsignment(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)


class Timetable(models.Model):

    class DaysChoices(models.IntegerChoices):
        LUNI = 1, "Luni"
        MARTI = 2, "Marti"
        MIERCURI = 3, "Miercuri"
        JOI = 4, "Joi"
        VINERI = 5, "Vineri"
    day = models.IntegerField(choices=DaysChoices.choices, verbose_name="DaysChoices",)

    class HoursChoices(models.IntegerChoices):
        FIRST = 1, "12:30 - 13:20"
        SECOND = 2, "13:30 - 14:20"
        THIRD = 3, "14:30 - 15:20"
        FOURTH = 4, "15:30 - 16:20"
        FIFTH = 5, "16:30 - 17:20"
        SIXTH = 6, "17:30 - 18:20"
        SEVENTH = 7, "18:30 - 19:20"
    hour = models.IntegerField(choices=HoursChoices.choices, verbose_name="HoursChoices",)
    
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.DaysChoices(self.day).label} | {self.HoursChoices(self.hour).label}"
    

class Grade(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)

    class GradesChoices(models.IntegerChoices):
        ONE = 1, "1"
        TWO = 2, "2"
        THREE = 3, "3"
        FOUR = 4, "4"
        FIVE = 5, "5"
        SIX = 6, "6"
        SEVEN = 7, "7"
        EIGHT = 8, "8"
        NINE = 9, "9"
        TEN = 10, "10"
    grade = models.IntegerField(choices=GradesChoices.choices, verbose_name="GradesChoices", blank=True)

    def __str__(self) -> str:
        return f"Student: {self.student_id.first_name} {self.student_id.last_name} | Subject: {self.subject_id.subject_name} | Grade: {self.grade}"
