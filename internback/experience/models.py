from django.db import models
from person.models import Person


class Experience(models.Model):
    title = models.CharField(max_length=255)
    company = models.TextField()
    years = models.CharField(max_length=4)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
