from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    founded = models.PositiveIntegerField(null=True, blank=True)
    stadium = models.CharField(max_length=120, blank=True)
    coach = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
