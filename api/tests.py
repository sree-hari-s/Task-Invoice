from django.test import TestCase
from .models import Invoice, InvoiceDetail

class InvoiceModelTest(TestCase):

    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-01-01', customer_name='Test Customer')

    def test_invoice_creation(self):
        self.assertEqual(self.invoice.date, '2024-01-01')
        self.assertEqual(self.invoice.customer_name, 'Test Customer')

class InvoiceDetailModelTest(TestCase):

    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-01-01', customer_name='Test Customer')
        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.invoice,
            description='Test Description',
            quantity=2,
            unit_price=10.50
        )

    def test_invoice_detail_creation(self):
        self.assertEqual(self.invoice_detail.description, 'Test Description')
        self.assertEqual(self.invoice_detail.quantity, 2)
        self.assertEqual(float(self.invoice_detail.unit_price), 10.50)

    def test_invoice_detail_price_calculation(self):
        expected_price = 2 * 10.50
        self.assertEqual(float(self.invoice_detail.price), expected_price)
