from django.db import models

# create blog models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField()
    body = models.TextField()

# add the blog app to the settings

# create a migration

# migrate


# Create your models here.
