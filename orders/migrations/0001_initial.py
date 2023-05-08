# Generated by Django 4.1 on 2023-05-08 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('tax', models.FloatField()),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.article')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price_with_tax', models.FloatField()),
                ('total_price_without_tax', models.FloatField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('order_items', models.ManyToManyField(to='orders.orderitem')),
            ],
        ),
    ]
