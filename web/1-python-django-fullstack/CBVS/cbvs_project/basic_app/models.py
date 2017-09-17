from django.db import models
from django.core.urlresolvers import reverse


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs={'pk': self.pk})


class Student(models.Model):
    """Model definition for Student."""

    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    student = models.ForeignKey(School, related_name='students')

    def __str__(self):
        return self.name