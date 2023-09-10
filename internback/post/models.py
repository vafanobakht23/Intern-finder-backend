from django.db import models
from person.models import Person


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
