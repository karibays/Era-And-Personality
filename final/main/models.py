from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=150)
    url = models.CharField(max_length=800)
    image_url = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name