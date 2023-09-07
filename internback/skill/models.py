from django.db import models
from person.models import Person


class Skill(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
