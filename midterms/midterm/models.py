from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    assigned_personnel =  models.CharField(max_length=255)
    due_date = models.DateField()
    status =  models.CharField(max_length=255, default='')

    # def status():
    #     if due_date < date.today():
    #         status =  models.CharField(max_length=255, default='Overdue')
    #     elif

    def __str__(self):
        return f"{self.title} {self.description} {self.assigned_personnel} {self.due_date} {self.status}"