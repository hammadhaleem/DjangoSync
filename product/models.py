from django.db import models

# Create your models here.

class item(models.Model):
    id     			=models.AutoField(primary_key=True)
    name   			=models.CharField(max_length=200)
    slug   			=models.CharField(max_length=200)
    text   			=models.TextField()
    created_by  	=models.CharField(max_length=200)
    timestamp    	=models.DateTimeField('date published')
    tags  			=models.CharField(max_length=400)
    photo			=models.CharField(max_length=200)
    video 			=models.CharField(max_length=200)
    time_to_deliver =models.Int() #In days 
  	cost 			=models.Float() #In Rupees 
  	category_id 	=models.Int()

    def __unicode__(self):
        return self.slug


class category(models.Model):
	id       =models.AutoField(primary_key=True)
	cat_name =models.CharField(max_length=200)
	cat_desc =models.TextField()
	cat_slug =models.CharField(max_length=200)

	def __unicode__(self):
        return self.cat_slug


