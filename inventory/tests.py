from django.test import TestCase
from rest_framework.test import APIClient
from .models import Item, Supplier


class InventoryAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name="Test Supplier", contact_info="1234567890")
        self.item = Item.objects.create(name="Test Item", description="Test Description", price=10.0)
        self.item.suppliers.add(self.supplier)

    def test_create_item(self):
        response = self.client.post('/api/items/', {
            'name': 'New Item',
            'description': 'New Description',
            'price': 15.0,
            'suppliers': [self.supplier.id]
        })
        self.assertEqual(response.status_code, 201)

    def test_get_items(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, 200)

    def test_create_supplier(self):
        response = self.client.post('/api/suppliers/', {
            'name': 'New Supplier',
            'contact_info': '9876543210'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_suppliers(self):
        response = self.client.get('/api/suppliers/')
        self.assertEqual(response.status_code, 200)
