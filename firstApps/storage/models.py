from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title

# Deadline Method for Tasks
def default_deadline():
    now = datetime.now()
    deadline = now.replace(hour=19, minute=0, second=0, microsecond=0)
    return deadline if deadline > now else deadline + timedelta(days=1)
  

class Task(Note):
   deadline = models.DateTimeField(default=default_deadline)
   done = models.BooleanField()