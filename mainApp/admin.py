from django.contrib import admin
from .models import * # To add all tables

# Register your models here.
admin.site.register(
    (
        Buyer,
        Maincategory,
        Subcategory,
        Brand,
        Product,
        Checkout,
        CheckoutProducts,
    )
)
