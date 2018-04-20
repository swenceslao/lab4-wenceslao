from django.db import models

# Create your models here.

class User(models.Model):
	email = models.EmailField()
	first_name = models.CharField(max_length=30, help_text="First name")
	last_name = models.CharField(max_length=30, help_text="Last name")
	shipping_address = models.CharField(max_length=300, help_text="Shipping address")

	def __str__(self):
		return '%s %s (%s)' % (self.first_name, self.last_name, self.email)

class Product(models.Model):
	price = models.DecimalField(max_digits=9, decimal_places=2)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=300)

	def __str__(self):
		return '%s (PHP %s)' % (self.name, self.price)

class Cart(models.Model):
	cart_code = models.CharField(max_length=10)
	total_price = models.DecimalField(max_digits=11, decimal_places=2)
	paid = models.BooleanField()
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.cart_code