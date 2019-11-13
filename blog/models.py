from django.db import models

# create blog models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField()
    body = models.TextField()

    def summary(self):
        return self.body[:100] + '...'

    def pub_date_pretty(self):
        return self.publish_date.strftime("%b %d %Y")
