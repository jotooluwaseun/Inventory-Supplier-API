from django.db import models


# Inventory model
class Inventory(models.Model):
    CURRENCY=(
        ('NGN', 'Naira'),
    )   

    item_name = models.CharField(max_length=100)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    currency = models.CharField(max_length=3, choices=CURRENCY, default="NGN")
    date_created = models.DateTimeField(auto_now=True)
    supplier_id = models.ForeignKey('Supplier', on_delete=models.CASCADE, db_column='supplier_id')

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name_plural = "Inventory"
        db_table = "inventory"

# Supplier model
class Supplier(models.Model):
    CITIES = (
        ("LA", "Lagos"),
        ("IB", "Ibadan"),
    )

    COUNTRIES = (
        ("NG", "Nigeria"),
        )

    supplier_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    alt_phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=255)    
    country = models.CharField(max_length=2, choices=COUNTRIES, default='NG')
    city = models.CharField(max_length=2, choices=CITIES)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.supplier_name

    class Meta:
        verbose_name_plural = "Supplier"
        db_table = "supplier"
