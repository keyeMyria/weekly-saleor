# Generated by Django 2.0.3 on 2018-03-26 18:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0053_product_seo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('name', models.CharField(max_length=60, validators=[django.core.validators.MaxLengthValidator(60)]))
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='notes',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.ProductNote'),
        ),
    ]
