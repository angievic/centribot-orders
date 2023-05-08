from django.test import TestCase
from orders.models import Article,Order,OrderItem
from django.test import Client


class ArticleTest(TestCase):
    def setUp(self):
        Article.objects.create(
            reference="123asd",
            name="pants",
            description="blue jeans",
            price=30000,
            tax=0.1
            )
        Article.objects.create(
            reference="456fgh",
            name="box",
            description="4x4",
            price=10000,
            tax=0.2
            )

    def test_article_creation(self):
        """Article created"""
        article = Article.objects.get(reference="123asd")
        self.assertEqual(article.name,"pants")
        self.assertEqual(article.tax, 0.1)

    def test_article_get(self):
        response = self.client.get("/article/")
        self.assertEqual(response.status_code,200)


class OrderTest(TestCase):
    def setUp(self):
        Article.objects.create(
            reference="123asd",
            name="pants",
            description="blue jeans",
            price=30000,
            tax=0.1
            )

    def test_article_creation(self):
        """Article created"""
        article = Article.objects.get(reference="123asd")
        self.assertEqual(article.name,"pants")
        self.assertEqual(article.tax, 0.1)

    def test_order_post(self):
        order_data = {
            "order_items": [
            {
                "reference": "123asd",
                "quantity": 10
            },
            {
                "reference": "456fgh",
                "quantity": 10
            }
            ]
        }
        response = self.client.post("/order/", order_data)
        self.assertEqual(response.status_code,200)
        order = Order.objects.all().first()
        self.assertEqual(order.total_price_with_tax,450000)
        self.assertEqual(order.total_price_without_tax, 400000)