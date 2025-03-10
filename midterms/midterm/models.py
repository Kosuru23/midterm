from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.DateField()
    status =  models.CharField(max_length=20, default='')

    def update(self):
        if self.due_date < date.today():
            self.status =  'Overdue'
        elif self.due_date == date.today():
            self.status = 'Due Today'
        else:
            self.status = 'Upcoming'

        self.save()

    def __str__(self):
        return f"{self.title} {self.description} {self.due_date} {self.status}"