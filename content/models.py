from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    slug =   models.CharField(max_length=200)
    text =   models.TextField()
    author = models.CharField(max_length=200)
    date =   models.DateTimeField('date published')
    tags =   models.CharField(max_length=200)
    def __unicode__(self):
        return self.slug


