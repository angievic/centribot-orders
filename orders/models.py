from django.db import models


class Article(models.Model):
    reference = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    tax = models.FloatField() #se guarda en formato decimal 5% es 0.05
    creation_date = models.DateField(auto_now_add=True)

class OrderItem(models.Model):
    article = models.ForeignKey(Article,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

class Order(models.Model):
    order_items = models.ManyToManyField(OrderItem, blank=True)
    total_price_with_tax = models.FloatField(blank=True, null=True)
    total_price_without_tax = models.FloatField(blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)

