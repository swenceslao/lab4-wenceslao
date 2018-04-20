from rest_framework import serializers
from .models import User, Cart, Product

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		# fields = ('id', 'email', 'first_name', 'last_name', 'shipping_address')
		fields = '__all__'

	class UserSerializer(serializers.Serializer):
		id = serializers.IntegerField(read_only=True)
		email = serializers.EmailField()
		first_name = serializers.CharField(max_length=30, help_text="First name")
		last_name = serializers.CharField(max_length=30, help_text="Last name")
		shipping_address = serializers.CharField(max_length=300, help_text="Shipping address")

		def create(self, validated_data):
		    return User.objects.create(**validated_data)

		def update(self, instance, validated_data):
		    instance.email = validated_data.get('email', instance.email)
		    instance.first_name = validated_data.get('first_name', instance.first_name)
		    instance.last_name = validated_data.get('last_name', instance.last_name)
		    instance.shipping_address = validated_data.get('shipping_address', instance.shipping_address)
		    instance.save()
		    return instance

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

	class ProductSerializer(serializers.Serializer):
		id = serializers.IntegerField(read_only=True)
		price = serializers.DecimalField(max_digits=9, decimal_places=2)
		name = serializers.CharField(max_length=30)
		description = serializers.CharField(max_length=300)

		def create(self, validated_data):
		    return Product.objects.create(**validated_data)

		def update(self, instance, validated_data):
		    instance.price = validated_data.get('price', instance.price)
		    instance.name = validated_data.get('name', instance.name)
		    instance.description = validated_data.get('description', instance.description)
		    instance.save()
		    return instance

class CartSerializer(serializers.ModelSerializer):
	products = ProductSerializer(many=True)

	class Meta:
		model = Cart
		fields = '__all__'

	class CartSerializer(serializers.Serializer):
		id = serializers.IntegerField(read_only=True)
		cart_code = serializers.CharField(max_length=10)
		total_price = serializers.DecimalField(max_digits=11, decimal_places=2)
		paid = serializers.BooleanField()

		def create(self, validated_data):
			products_data = validated_data.pop('products')
			cart = Cart.objects.create(**validated_data)
			for product_data in products_data:
				Product.object.create(cart=cart, **product_data)

			return cart

		def update(self, instance, validated_data):
		    instance.cart_code = validated_data.get('cart_code', instance.cart_code)
		    instance.total_price = validated_data.get('total_price', instance.total_price)
		    instance.paid = validated_data.get('paid', instance.paid)
		    products_data = validated_data.pop('products')
		    instance.products_data = products_data.id
		    return instance