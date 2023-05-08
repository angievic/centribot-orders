from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status


from orders.models import Article, Order, OrderItem
from orders.serializers import ArticleSerializer, OrderItemSerializer, OrderSerializer
from rest_framework import viewsets
# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing article instances.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing order items instances.
    """
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class OrderViewSet(viewsets.ViewSet):
    """
    A viewset for viewing and editing order instances.
    """

    def list(self, request):
        id_data = request.query_params.get('id')
        if id_data:
            order = Order.objects.get(id=id_data)
            if order:
                serializer = OrderSerializer(order, many=False)
                return Response(serializer.data)
            return Response({"error: Order does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        orders = Order.objects.all()
        if orders:
            return Response(OrderSerializer(orders,many=True).data)
        return Response({"message: empty "}, status=status.HTTP_200_OK)

    def create(self, request):
        """Create order with order items and calculate total price with/without tax"""
        order_items_data = request.data['order_items']
        order_items_result = []
        if order_items_data:
            total_price_with_tax = 0
            total_price_without_tax = 0
            for o in order_items_data:
                article = Article.objects.get(reference=o["reference"])
                if article:
                    orderitem = OrderItem(
                        article = article,
                        quantity = o["quantity"]
                    )
                    orderitem.save()
                    order_items_result.append(orderitem.id)
                    total_price_with_tax = total_price_with_tax + ((orderitem.article.price + (orderitem.article.price*orderitem.article.tax))*orderitem.quantity)
                    total_price_without_tax = total_price_without_tax + ((orderitem.article.price) * orderitem.quantity)
                else:
                    return Response({"error: Article does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            order = Order(
                total_price_with_tax = total_price_with_tax,
                total_price_without_tax = total_price_without_tax
            )
            order.save()
            order.order_items.add(*order_items_result)
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"error: Need to provide order items"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update order with new order items and calculate total price with/without tax"""
        order_items_data = request.data['order_items']
        order_id = request.data['order_id']
        order_items_result = []
        order = Order.objects.get(id=order_id)
        if order:
            if order_items_data:
                total_price_with_tax = 0
                total_price_without_tax = 0
                for o in order_items_data:
                    article = Article.objects.get(reference=o["reference"])
                    if article:
                        orderitem = OrderItem(
                            article = article,
                            quantity = o["quantity"]
                        )
                        orderitem.save()
                        order_items_result.append(orderitem.id)
                        total_price_with_tax = total_price_with_tax + ((orderitem.article.price + (orderitem.article.price*orderitem.article.tax))*orderitem.quantity)
                        total_price_without_tax = total_price_without_tax + ((orderitem.article.price) * orderitem.quantity)
                    else:
                        return Response({"error: Article does not exist"}, status=status.HTTP_400_BAD_REQUEST)
                order.total_price_with_tax = total_price_with_tax
                order.total_price_without_tax = total_price_without_tax
                order.order_items.clear()
                order.order_items.add(*order_items_result)
                order.save()
                return Response({"message": "success"}, status=status.HTTP_200_OK)
            else:
                return Response({"error: Need to provide order items"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error: Need to provide order id"}, status=status.HTTP_400_BAD_REQUEST)

            


