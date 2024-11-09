from django.contrib import admin
from .models import * # To add all tables

# Register your models here.
admin.site.register(
    (
        Buyer,
        Brand,
        Checkout,
        CheckoutProducts,
        Wishlist,   
        ContactUs,     
    )
)

@admin.register(Maincategory)
class Maincategory(admin.ModelAdmin):
    list_display = ("id","name")

@admin.register(Subcategory)
class Subcategory(admin.ModelAdmin):
    list_display = ("id","name")
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("id","name","maincategory","subcategory","brand","color","size","baseprice","discount","finalprice","pic1","pic2","pic3","pic4")

