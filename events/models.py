from django.db import models
from clubs.models import Club

# Create your models here.

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=150)
    date = models.DateField()
    venue = models.CharField(max_length=200)
    club = models.ForeignKey(Club,on_delete=models.PROTECT)
    status = models.CharField(max_length=20,
                              choices=[("upcoming", "Upcoming"),
                                       ("completed", "Completed"),
                                       ("cancelled", "Cancelled"),],
                              default="upcoming")

    def __str__(self):
        return self.event_name