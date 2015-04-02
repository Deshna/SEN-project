from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
	name = models.CharField(max_length = 30)
	description = models.CharField(max_length = 300)
	categoryID = models.IntegerField(primary_key = True)

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length = 30,primary_key = True)
	category = models.ForeignKey(Category)

	def __str__(self):              
		return self.name

class Product(models.Model):
	image = models.ImageField(upload_to = 'media/', blank = True, null = True) #, height_field = '', width_field = '')
	name = models.CharField(max_length = 30)
	price = models.IntegerField()
	productID = models.IntegerField(primary_key = True)
	description = models.CharField(max_length = 300)
	unitsInStock = models.IntegerField()
	unitsInOrder = models.IntegerField()
	#COLOR_CHOICES = ((RED,'RED'),(BLUE,'BLUE'),(BLACK,'BLACK'),)
	color = models.CharField(max_length = 10)
	work = models.CharField(max_length = 30)
	fabric = models.CharField(max_length = 30)
	style = models.CharField(max_length = 30)
	occasion = models.CharField(max_length = 30)

	def __str__(self):             
		return self.productID

class Order(models.Model):
	orderID = models.IntegerField(primary_key = True)
	customerID = models.IntegerField()
	orderDate = models.IntegerField()
	shipperID = models.IntegerField()
	billID = models.IntegerField()
	totalprice = models.IntegerField()

	def __str__(self):              
		return self.orderID

class OrderProduct(models.Model):
	productID = models.OneToOneField(Product)
	order = models.ForeignKey(Order)

