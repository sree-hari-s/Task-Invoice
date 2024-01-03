from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

@api_view(["GET", "POST"])
def invoices_list_create(request):
    if request.method == "GET":
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        print("Request data:", request.data)
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            print("Validated data:", serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def invoices_detail(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        invoice_details = InvoiceDetail.objects.filter(invoice=invoice)
        
        invoice_serializer = InvoiceSerializer(invoice)
        details_serializer = InvoiceDetailSerializer(invoice_details, many=True)

        result_data = {
            'invoice': invoice_serializer.data,
            'invoice_details': details_serializer.data
        }

        return Response(result_data)

    elif request.method == "PUT":
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
