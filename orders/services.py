
from orders.models import Article, Order, OrderItem
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction


@transaction.atomic
def update_orders(order_id,order_items_data):
    order_items_result = []
    order = Order.objects.get(id=order_id)
    if not order:
        return Response({"error: Need to provide order id"}, status=status.HTTP_400_BAD_REQUEST)
    if not order_items_data:
        return Response({"error: Need to provide order items"}, status=status.HTTP_400_BAD_REQUEST)
    total_price_with_tax = 0
    total_price_without_tax = 0
    try:
        for o in order_items_data:
            article = Article.objects.get(reference=o["reference"])
            if not article:
                return Response({"error: Article does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            orderitem = OrderItem(article = article,quantity = o["quantity"])
            orderitem.save()
            order_items_result.append(orderitem.id)
            total_price_with_tax += ((orderitem.article.price + (orderitem.article.price*orderitem.article.tax))*orderitem.quantity)
            total_price_without_tax += ((orderitem.article.price) * orderitem.quantity)
        order.total_price_with_tax = total_price_with_tax
        order.total_price_without_tax = total_price_without_tax
        order.order_items.clear()
        order.order_items.add(*order_items_result)
        order.save()
    except Exception as e:
            # Rollback the transaction in case of an error
        transaction.set_rollback(True)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"message": "success"}, status=status.HTTP_200_OK)



@transaction.atomic
def create_orders(order_items_data):
    order_items_result = []
    if not order_items_data:
        return Response({"error: Need to provide order items"}, status=status.HTTP_400_BAD_REQUEST)
    total_price_with_tax = 0
    total_price_without_tax = 0
    try:
        for o in order_items_data:
            article = Article.objects.get(reference=o["reference"])
            if not article:
                return Response({"error: Article does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            orderitem = OrderItem(article = article,quantity = o["quantity"])
            orderitem.save()
            order_items_result.append(orderitem.id)
            total_price_with_tax += ((orderitem.article.price + (orderitem.article.price*orderitem.article.tax))*orderitem.quantity)
            total_price_without_tax += ((orderitem.article.price) * orderitem.quantity)
        order = Order(
            total_price_with_tax = total_price_with_tax,
            total_price_without_tax = total_price_without_tax
        )
        order.save()
        order.order_items.add(*order_items_result)
    except Exception as e:
            # Rollback the transaction in case of an error
        transaction.set_rollback(True)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"message": "success"}, status=status.HTTP_200_OK)