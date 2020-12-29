from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    food_id = models.AutoField
    food_name = models.CharField(max_length=50 , default="")
    cateory = models.CharField(max_length=50 , default="")
    subcategory = models.CharField(max_length=50 , default = "")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'menu/images' , default="")
    
    def __str__(self):
        return self.food_name

class Productbf(models.Model):
	food_id = models.AutoField
	food_name = models.CharField(max_length=50 , default="")
	cateory = models.CharField(max_length=50 , default="")
	subcategory = models.CharField(max_length=50 , default = "")
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to = 'menu/images' , default="")

	def __str__(self):
		return self.food_name
        
class Productbev(models.Model):
	food_id = models.AutoField
	food_name = models.CharField(max_length=50 , default="")
	cateory = models.CharField(max_length=50 , default="")
	subcategory = models.CharField(max_length=50 , default = "")
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to = 'menu/images' , default="")

	def __str__(self):
		return self.food_name

class Productchp(models.Model):
	food_id = models.AutoField
	food_name = models.CharField(max_length=50 , default="")
	cateory = models.CharField(max_length=50 , default="")
	subcategory = models.CharField(max_length=50 , default = "")
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to = 'menu/images' , default="")

	def __str__(self):
		return self.food_name

class Productsoup(models.Model):
	food_id = models.AutoField
	food_name = models.CharField(max_length=50 , default="")
	cateory = models.CharField(max_length=50 , default="")
	subcategory = models.CharField(max_length=50 , default = "")
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to = 'menu/images' , default="")

	def __str__(self):
		return self.food_name

class Productdessert(models.Model):
	food_id = models.AutoField
	food_name = models.CharField(max_length=50 , default="")
	cateory = models.CharField(max_length=50 , default="")
	subcategory = models.CharField(max_length=50 , default = "")
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to = 'menu/images' , default="")

	def __str__(self):
		return self.food_name


class Customer(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE ,  null=True , blank = True)
	name = models.CharField(max_length = 200 , null = True)
	email = models.CharField(max_length=200 , null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer , on_delete=models.SET_NULL , blank=True , null=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False , null=True , blank=False)
	transaction_id = models.CharField(max_length=200 , null=True)

	def __str__(self):
		return str(self.id)
	
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		orderitemsbf = self.orderitembf_set.all()
		totalbf = sum([item.get_total for item in orderitemsbf])
		chp = self.orderitemchp_set.all()
		total_chp = sum([item.get_total for item in chp])
		soup = self.orderitemsoup_set.all()
		total_soup = sum([item.get_total for item in soup])
		dessert = self.orderitemdessert_set.all()
		total_dessert = sum([item.get_total for item in dessert])
		bev = self.orderitembev_set.all()
		total_bev = sum([item.get_total for item in bev])
		total_main = total + totalbf + total_chp + total_soup + total_dessert + total_bev
		return total_main

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		orderitemsbf = self.orderitembf_set.all() 
		totalbf = sum([item.quantity for item in orderitemsbf])
		chp = self.orderitemchp_set.all()
		total_chp = sum([item.quantity for item in chp])
		soup = self.orderitemsoup_set.all()
		total_soup = sum([item.quantity for item in soup])
		dessert = self.orderitemdessert_set.all()
		total_dessert = sum([item.quantity for item in dessert])
		bev = self.orderitembev_set.all()
		total_bev =  sum([item.quantity for item in bev])
		
		 

		total_main = total + totalbf + total_chp + total_soup + total_dessert + total_bev
		
		return total_main

class OrderItem(models.Model):
	product = models.ForeignKey(Product  , on_delete=models.SET_NULL , blank=True , null=True)
	order = models.ForeignKey(Order , on_delete=models.SET_NULL , blank=True , null=True)
	quantity = models.IntegerField(default=0 , null=True , blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

	def __str__(self):
		return self.product.food_name

class OrderItembf(models.Model):
	product = models.ForeignKey(Productbf  , on_delete=models.SET_NULL , blank=True , null=True)
	order = models.ForeignKey(Order , on_delete=models.SET_NULL , blank=True , null=True)
	quantity = models.IntegerField(default=0 , null=True , blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class OrderItembev(models.Model):
	product = models.ForeignKey(Productbev  , on_delete=models.SET_NULL , blank=True , null=True)
	order = models.ForeignKey(Order , on_delete=models.SET_NULL , blank=True , null=True)
	quantity = models.IntegerField(default=0 , null=True , blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class OrderItemchp(models.Model):
	product = models.ForeignKey(Productchp  , on_delete=models.SET_NULL , blank=True , null=True)
	order = models.ForeignKey(Order , on_delete=models.SET_NULL , blank=True , null=True)
	quantity = models.IntegerField(default=0 , null=True , blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class OrderItemsoup(models.Model):
	product = models.ForeignKey(Productsoup  , on_delete=models.SET_NULL , blank=True , null=True)
	order = models.ForeignKey(Order , on_delete=models.SET_NULL , blank=True , null=True)
	quantity = models.IntegerField(default=0 , null=True , blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class OrderItemdessert(models.Model):
	product = models.ForeignKey(Productdessert  , on_delete=models.SET_NULL , blank=True , null=True)
	order = models.ForeignKey(Order , on_delete=models.SET_NULL , blank=True , null=True)
	quantity = models.IntegerField(default=0 , null=True , blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total