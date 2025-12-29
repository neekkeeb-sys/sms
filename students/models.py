from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name  = models.CharField(max_length=100)
    roll  = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.roll})"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lectures_attended = models.IntegerField()
    total_lectures    = models.IntegerField()

class Marks(models.Model):
    student   = models.ForeignKey(Student, on_delete=models.CASCADE)
    physics   = models.IntegerField()
    chemistry = models.IntegerField()
    maths     = models.IntegerField()

class Notice(models.Model):
    message      = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
