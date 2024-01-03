from django.urls import path
from .views import invoices_list_create, invoices_detail

urlpatterns = [
    path("invoices/", invoices_list_create, name="invoices-list-create"),
    path("invoices/<int:pk>/", invoices_detail, name="invoices-detail"),
]
