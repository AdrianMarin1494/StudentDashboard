from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    mail = models.EmailField(max_length=255, null=False, unique=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    

class Classroom(models.Model):

    class YearChoices(models.IntegerChoices):
        I = 1, "I"
        II = 2, "II"
        III = 3, "III"
        IV = 4, "IV"
        V = 5, "V"
        VI = 6, "VI"
        VII = 7, "VII"
        VIII = 8, "VIII"
        IX = 9, "IX"
        X = 10, "X"
        XI = 11, "XI"
        XII = 12, "XII"
    year = models.IntegerField(choices=YearChoices.choices, verbose_name="Study Year", null=False, default=1)

    letter = models.CharField(max_length=1, null=False) 
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['year', 'letter'], name='unique_classroom_name')]


    def __str__(self) -> str:
        class_name = f"{self.YearChoices(self.year).label}-{self.letter}"
        return class_name
    

class Subject(models.Model):
    subject_name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self) -> str:
        return self.subject_name
    

class Student(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    class_id = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class ClassAsignment(models.Model):
    class_id = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['class_id', 'subject_id'], name='unique_classroom_subject')]

    def __str__(self) -> str:
        return f"{self.teacher_id.last_name} is teaching {self.subject_id.subject_name} at class {self.class_id}."


class Timetable(models.Model):

    class DaysChoices(models.IntegerChoices):
        LUNI = 1, "Luni"
        MARTI = 2, "Marti"
        MIERCURI = 3, "Miercuri"
        JOI = 4, "Joi"
        VINERI = 5, "Vineri"
    day = models.IntegerField(choices=DaysChoices.choices, verbose_name="Day",)

    class HoursChoices(models.IntegerChoices):
        FIRST = 1, "07:30 - 08:20"
        SECOND = 2, "08:30 - 09:20"
        THIRD = 3, "09:30 - 10:20"
        FOURTH = 4, "10:30 - 11:20"
        FIFTH = 5, "11:30 - 12:20"
        SIXTH = 6, "12:30 - 13:20"
        SEVENTH = 7, "13:30 - 14:20"
        EIGTH = 8, "14:30 - 15:20"
        NINTH = 9, "15:30 - 16:20"
        TENTH = 10, "16:30 - 17:20"
        ELEVENTH = 11, "17:30 - 18:20"
        TWELVTH = 12, "18:30 - 19:20"

    hour = models.IntegerField(choices=HoursChoices.choices, verbose_name="HoursChoices",)
    
    class_id = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    class Meta:
        # Adding constraints because a classroom can have only one subject assigned for a certain day/hour combination. (Eg. Classroom XII-A can only have Chemestry at 12:30 on a Monday. It is impossible for XII-A to have Math at the same time.)
        constraints = [models.UniqueConstraint(fields=['day', 'hour', 'class_id'], name='unique_classroom_assignment')]

    def __str__(self) -> str:
        return f"{self.DaysChoices(self.day).label} | {self.HoursChoices(self.hour).label}"
    
    

class Grade(models.Model):
    class_id = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)
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
