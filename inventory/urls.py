from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from inventory import views

router = DefaultRouter()
router.register("inventory", views.InventoryViewSet)
router.register("supplier", views.SupplierViewSet)

app_name = "inventory"

urlpatterns = [
    path("", include(router.urls)),
]
