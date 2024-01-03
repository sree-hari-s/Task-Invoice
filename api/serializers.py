from rest_framework import serializers
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ["id", "invoice", "description", "quantity", "unit_price", "price"]
        extra_kwargs = {
            "invoice": {"required": False, "allow_null": True}
        }
    
    def create(self, validated_data):
        print(validated_data)
        return InvoiceDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(validated_data)
        instance.description = validated_data.get("description", instance.description)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.unit_price = validated_data.get("unit_price", instance.unit_price)
        instance.save()
        return instance


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = InvoiceDetailSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = ["id", "date", "customer_name", "invoice_details"]

    def create(self, validated_data):
        invoice_details_data = validated_data.pop("invoice_details", [])
        invoice = Invoice.objects.create(**validated_data)

        self.create_or_update_invoice_details(invoice, invoice_details_data)

        invoice.refresh_from_db()
        serializer = self.__class__(invoice)
        return serializer.data

    def update(self, instance, validated_data):
        instance.date = validated_data.get("date", instance.date)
        instance.customer_name = validated_data.get("customer_name", instance.customer_name)
        instance.save()

        invoice_details_data = validated_data.get("invoice_details", [])
        self.create_or_update_invoice_details(instance, invoice_details_data)

        return instance

    def create_or_update_invoice_details(self, invoice, invoice_details_data):
        for detail_data in invoice_details_data:
            detail_id = detail_data.get("id")
            detail_data["invoice"] = invoice.id

            if detail_id:
                detail = InvoiceDetail.objects.get(id=detail_id, invoice=invoice)
                detail.description = detail_data.get("description", detail.description)
                detail.quantity = detail_data.get("quantity", detail.quantity)
                detail.unit_price = detail_data.get("unit_price", detail.unit_price)
                detail.save()
            else:
                InvoiceDetail.objects.create(
                    description=detail_data["description"],
                    quantity=detail_data["quantity"],
                    unit_price=detail_data["unit_price"],
                    invoice=invoice,  
                )
    def to_representation(self, instance):
        data = super().to_representation(instance)
        details_serializer = InvoiceDetailSerializer(instance.invoice_details.all(), many=True)
        data['invoice_details'] = details_serializer.data
        return data
    