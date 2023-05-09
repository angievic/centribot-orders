from orders.services import create_orders, update_orders
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
        """"List orders by id and all orders"""
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
        return create_orders(order_items_data)


    def update(self, request, pk=None):
        """Update order with new order items and calculate total price with/without tax"""
        order_items_data = request.data['order_items']
        order_id = request.data['order_id']
        return update_orders(order_id,order_items_data)
        
       
           

