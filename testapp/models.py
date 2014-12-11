from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class repos(models.Model):
    #slug = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    #ispublic = models.BooleanField()
    title = models.CharField(max_length=200)
    #commits = ListField()
    #files = ListField()
    #contributors = ListField()
    #updated = models.DateTimeField()
    created = models.DateTimeField()



