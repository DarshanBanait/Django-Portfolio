from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    gist = models.TextField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name
