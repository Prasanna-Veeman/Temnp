from django.db import models

# Create your models here.


class Products(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=5,decimal_places=2)
	image = models.ImageField(upload_to='images/',default='default.jpg')
	ctime = models.DateTimeField(auto_now_add=True)
	uptime = models.DateTimeField(auto_now=True)

	

class Shops(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	location = models.TextField()