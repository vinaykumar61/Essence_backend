from django.db import models

# Table1: Stores information about buyers
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)  # Name of the buyer
    username = models.CharField(max_length=50)  # Username for login
    email = models.CharField(max_length=50)  # Email of the buyer
    phone = models.CharField(max_length=15)  # Contact phone number
    addressline1 = models.CharField(max_length=50)  # First line of address
    addressline2 = models.CharField(max_length=50, blank=True, null=True)  # Optional second line of address
    addressline3 = models.CharField(max_length=50, blank=True, null=True)  # Optional third line of address
    pin = models.CharField(max_length=10)  # Postal code
    city = models.CharField(max_length=30)  # City of the buyer
    state = models.CharField(max_length=30)  # State of the buyer
    pic = models.ImageField(upload_to="user")  # Profile picture of the buyer
    
# Table2: Stores product main categories (e.g., Male, Female, Kids)
class Maincategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)  # Unique main category name

    #Maincategory object 1 ko Male,Female ,kids m show karne k liye 
    def __str__(self):
        return self.name
# Table3: Stores product subcategories (e.g., Jeans, Shirts, T-Shirts)
class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)  # Unique subcategory name

    def __str__(self):
        return self.name
    
# Table4: Stores information about product brands
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)  # Unique brand name
    pic = models.ImageField(upload_to="brand")  # Brand logo or image

    def __str__(self):
        return self.name
    
# Table5: Stores product details
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)  
    maincategory = models.ForeignKey(Maincategory, on_delete=models.CASCADE)  # Foreign key to main category
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)  # Foreign key to subcategory
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # Foreign key to brand
    color = models.CharField(max_length=20)  
    size = models.CharField(max_length=10)  
    baseprice = models.IntegerField()  
    discount = models.IntegerField()  
    finalprice = models.IntegerField()  
    stock = models.BooleanField(default=True)  # Whether the product is in stock or not
    description = models.TextField() 
    pic1 = models.ImageField(upload_to="product") 
    pic2 = models.ImageField(upload_to="product")  
    pic3 = models.ImageField(upload_to="product", default="", blank=True, null=True) 
    pic4 = models.ImageField(upload_to="product", default="", blank=True, null=True)  

    def __str__(self):
        return self.name