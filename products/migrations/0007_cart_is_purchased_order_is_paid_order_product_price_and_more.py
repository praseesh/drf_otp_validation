# Generated by Django 5.1.2 on 2024-11-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_status_order_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_purchased',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='product_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='qty',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('razorpay', 'Razorpay'), ('cod', 'Cash on Delivery'), ('paypal', 'PayPal')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]