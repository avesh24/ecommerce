# Generated by Django 4.1.3 on 2022-12-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_contact_alter_product_category_payment_orderplaced'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IC', 'Ice-Creams'), ('ML', 'Milk'), ('CZ', 'Cheese'), ('CR', 'Curd'), ('PN', 'Paneer'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('GH', 'Ghee')], max_length=2),
        ),
    ]
