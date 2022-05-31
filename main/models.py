from django.db import models

# Create your models here.
class Feedback(models.Model):
    user_name = models.CharField(max_length=120)
    email = models.EmailField()
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class ClgInfoIntents(models.Model):
    tag = models.CharField(max_length=140)
    patterns = models.CharField(max_length=140)
    responses = models.CharField(max_length=140)

# class Librarydb(models.Model):