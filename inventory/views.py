from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventory, Supplier
from .serializers import InventorySerializer, SupplierSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    """View to manage inventory APIs."""

    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()    

    def get_serializer_class(self):
        # Return the serializer class for the request
        if self.action == "list":
            return InventorySerializer
        return self.serializer_class


class SupplierViewSet(viewsets.ModelViewSet):
    """View to manage supplier APIs."""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

    def get_serializer_class(self):
        # Return the serializer class for the request
        if self.action == "list":
            return SupplierSerializer
        return self.serializer_class
