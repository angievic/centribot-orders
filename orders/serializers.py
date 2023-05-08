from orders.models import Article, Order, OrderItem
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    article_reference = serializers.RelatedField(source='article_reference', read_only=True)
    class Meta:
        model = OrderItem
        fields = ('id', 'article', 'article_reference','quantity','order_id')
        depth = 2

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','order_items','total_price_with_tax','total_price_without_tax','creation_date')
        depth = 2