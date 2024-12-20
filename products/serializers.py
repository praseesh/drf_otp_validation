from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import Address
from .models import Cart, Payment, Product, Category, Order

class ProductCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'brand', 'price', 'related_products',
                  'stock_quantity', 'image']
    
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError('Product name cannot be empty.')
        if len(value) > 255:
            raise serializers.ValidationError("Product name cannot be longer than 255 characters.")
        return value

    def validate_category(self, value):
        if not Category.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Selected category does not exist.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value

    def validate_stock_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Stock quantity must be greater than zero.")
        return value

    def validate_rating(self, value):
        if value < 0.0 or value > 5.0:
            raise serializers.ValidationError("Rating must be between 0.0 and 5.0.")
        return value
    def validate_image(self, image):
        max_size_mb = 5
        if image.size > max_size_mb * 1024 * 1024:
            raise serializers.ValidationError(f"Image size must be less than {max_size_mb} MB.")
        valid_extensions = ['.png', '.jpg', '.jpeg']
        if not any([image.name.lower().endswith(ext) for ext in valid_extensions]):
            raise serializers.ValidationError(f"Supported image formats are: {', '.join(valid_extensions)}")

        return image

    def validate_related_products(self, value):
        if self.instance and self.instance.id in [product.id for product in value.all()]:
            raise serializers.ValidationError("A product cannot be related to itself.")
        return value
class CategoryCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        
class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductUpdationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'brand', 'price', 'related_products',
                  'stock_quantity', 'image']
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError('Product name cannot be empty.')
        if len(value) > 255:
            raise serializers.ValidationError("Product name cannot be longer than 255 characters.")
        return value

    def validate_category(self, value):
        if not Category.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Selected category does not exist.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value

    def validate_stock_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Stock quantity must be greater than zero.")
        return value

    def validate_rating(self, value):
        if value < 0.0 or value > 5.0:
            raise serializers.ValidationError("Rating must be between 0.0 and 5.0.")
        return value

    def validate_related_products(self, value):
        if self.instance and self.instance.id in [product.id for product in value.all()]:
            raise serializers.ValidationError("A product cannot be related to itself.")
        return value
    
#                                             C A R T                                                         
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity', 'is_purchased', 'created_at', 'updated_at']
        read_only_fields = ['id', 'is_purchased', 'created_at', 'updated_at']

    def validate_quantity(self, value):
        """
        Validate the quantity field to ensure no more than 5 items are added.
        """
        if value > 5:
            raise serializers.ValidationError("Only 5 items can be added for each product.")
        return value

     
"""                                             O R D E R                                                         """
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'payment_status', 'paid_at']

class OrderSerializer(serializers.Serializer):
    is_cart = serializers.BooleanField(required=False, default=False)
    product_id = serializers.IntegerField(required=False, allow_null=True)
    address_id = serializers.IntegerField(required=True)  
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, allow_null=True)
    qty = serializers.IntegerField(required=True, min_value=1, max_value=5) 
    payment_method = serializers.ChoiceField(choices=['razorpay', 'cod', 'paypal'])

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'order_status', 'total_price', 'payment_method', 
            'created_at', 'updated_at', 'items', 'payment', 'is_cart',
            'product_id', 'address_id', 'product_price', 'qty'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        is_cart = self.initial_data.get('is_cart', False)
        if is_cart:
            self.fields['qty'].required = False
        else:
            self.fields['qty'].required = True
            
    def validate_address(self, value):
        if not Address.objects.filter(id=value.id).exists():
            raise ValidationError("The provided address does not exist.")
        return value


