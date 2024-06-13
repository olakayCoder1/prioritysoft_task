from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Item, Supplier


class InventoryAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name="Test Supplier", contact_info="1234567890")
        self.item = Item.objects.create(name="Test Item", description="Test Description", price=10.0)
        self.item.suppliers.add(self.supplier)
        

    def test_create_item(self):
        url = reverse('item-list')
        response = self.client.post(url, {
            'name': 'New Item',
            'description': 'New Description',
            'price': 15.0,
            'suppliers': [self.supplier.id]
        })
        self.assertEqual(response.status_code, 201)

    def test_update_item(self):
        url = reverse('item-detail', args=[self.item.id])
        response = self.client.put(url, {
            'name': 'Updated Item',
            'description': 'Updated Description',
            'price': 20.0,
            'suppliers': [self.supplier.id]
        })
        self.assertEqual(response.status_code, 200)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')

    def test_get_items(self):
        url = reverse('item-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_supplier(self):
        url = reverse('supplier-list')
        response = self.client.post(url, {
            'name': 'New Supplier',
            'contact_info': '9876543210'
        })
        self.assertEqual(response.status_code, 201)

    def test_update_supplier(self):
        url = reverse('supplier-detail', args=[self.supplier.id])
        response = self.client.put(url, {
            'name': 'Updated Supplier',
            'contact_info': '9999999999'
        })
        self.assertEqual(response.status_code, 200)
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'Updated Supplier')

    def test_get_suppliers(self):
        url = reverse('supplier-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_suppliers_for_item(self):
        url = reverse('item-suppliers', args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


    def test_get_items_for_supplier(self):
        url = reverse('supplier-items', args=[self.supplier.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)