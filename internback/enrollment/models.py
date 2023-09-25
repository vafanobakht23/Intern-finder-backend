from django.db import models
from post.models import Post
from person.models import Person


class Enrollment(models.Model):
    status = models.CharField(max_length=2)
    answers = models.TextField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
