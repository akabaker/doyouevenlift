from django.db import models
from django.core.urlresolvers import reverse

class Workout(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workouts-view', kwargs={'pk': self.id})

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    workout = models.ForeignKey(Workout)

    def __str__(self):
        return self.name

class Set(models.Model):
    exercise = models.ForeignKey(Exercise)
    reps = models.IntegerField(max_length=2)
    max_reps = models.IntegerField(max_length=2)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.max_reps
