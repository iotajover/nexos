from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.name)

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)
    def __str__(self):
        return str(self.id) + ' - ' + str(self.name)

class Score(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    studen = models.ForeignKey(Student, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=14, decimal_places=4)