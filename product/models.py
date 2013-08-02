from django.db import models



class category(models.Model):
    self.id=models.AutoField(primary_key=True)
    self.cat_name=models.CharField(max_length=200)
    self.cat_desc=models.TextField()
    self.cat_slug=models.CharField(max_length=200)

    def __unicode__(self):
        return self.cat_slug


class item(models.Model):
    self.id=models.AutoField(primary_key=True)
    self.name=models.CharField(max_length=200)
    self.slug=models.CharField(max_length=200)
    self.text=models.TextField()
    self.created_by=models.CharField(max_length=200)
    self.timestamp=models.DateTimeField('date published')
    self.tags=models.CharField(max_length=400)
    self.photo=models.CharField(max_length=200)
    self.video=models.CharField(max_length=200)
    self.time_to_deliver=models.IntegerField(default=1) #In days 
    self.cost=models.IntegerField(default=1) #In Rupees 
    self.category_id=models.ForeignKey(category.id) #Key 
    #models.IntegerField(default=0)

    def __unicode__(self):
        return self.slug


