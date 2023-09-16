from django.db import models
from post.models import Post


class Exam(models.Model):
    content = models.TextField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content
