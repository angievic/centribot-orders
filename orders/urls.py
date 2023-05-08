from orders.views import ArticleViewSet, OrderItemViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')
router.register(r'orderitem', OrderItemViewSet, basename='order_item')
router.register(r'order', OrderViewSet, basename='order')
urls_orders= router.urls