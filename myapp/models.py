from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    #required by the auth model
    user = models.OneToOneField(User, unique=True)
    fullname = models.CharField(max_length=30, null=True, blank=True)
    length_blouse = models.IntegerField(null = True, blank = True)
    waist_blouse = models.IntegerField(null = True, blank = True)
    sleeve_length = models.IntegerField(null = True, blank = True)
    neck_front = models.IntegerField(null = True, blank = True)
    bust = models.IntegerField(null = True, blank = True)
    shoulder = models.IntegerField(null = True, blank = True)
    sleeve_width = models.IntegerField(null = True, blank = True)
    neck_back = models.IntegerField(null = True, blank = True)
    address_line1= models.CharField(max_length=100, null=True, blank=True)
    address_line2= models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.IntegerField(max_length=10,null=True,blank=True)
    cardname = models.CharField(max_length=100, null=True, blank=True)
    cardno = models.IntegerField(null=True,blank=True)
    exp_month = models.CharField(max_length=50, null=True, blank=True)
    exp_year = models.IntegerField(null=True,blank=True)
    cvv = models.IntegerField(null=True,blank=True)
    pastorders_no = models.CommaSeparatedIntegerField(max_length = 40, null = True, blank = True)
    wishlist = models.CommaSeparatedIntegerField(max_length = 40, null = True, blank = True)
    cart = models.CommaSeparatedIntegerField(max_length = 40, null = True, blank = True)

class Category(models.Model):
	name = models.CharField(max_length = 30)
	description = models.CharField(max_length = 300)
	categoryID = models.IntegerField(primary_key = True)

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length = 30,primary_key = True)
	category = models.ForeignKey(Category)
	SubCategoryID = models.IntegerField(null = True, blank = True)


	def __str__(self):              
		return self.name

class Product(models.Model):
	#image = models.ImageField(upload_to = 'media/', blank = True, null = True) #, height_field = '', width_field = '')
	path = models.CharField(max_length=512)
	name = models.CharField(max_length = 30)
	name_clean = models.CharField(max_length = 30, null = True, blank = True)
	price = models.IntegerField()
	productID = models.IntegerField(primary_key = True)
	description = models.CharField(max_length = 300,default = "none")
	unitsInStock = models.IntegerField(default = 0)
	unitsInOrder = models.IntegerField(default = 0)
	#COLOR_CHOICES = ((RED,'RED'),(BLUE,'BLUE'),(BLACK,'BLACK'),)
	color = models.CharField(max_length = 10)
	work = models.CharField(max_length = 30, default = "none")
	fabric = models.CharField(max_length = 30, default = "", blank = True, null = True)
	style = models.CharField(max_length = 30, default = "", blank = True, null = True)
	occasion = models.CharField(max_length = 30, default = "", blank = True, null = True)
	subcategory = models.ForeignKey(SubCategory, null = True)
	views = models.IntegerField(null = True)

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

class Mailinglist(models.Model):
	mail = models.CharField(max_length = 50, null = True)