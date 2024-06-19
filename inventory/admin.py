from django.contrib import admin
from .models import Inventory, Supplier

# Registered models
admin.site.register(Inventory)
admin.site.register(Supplier)
