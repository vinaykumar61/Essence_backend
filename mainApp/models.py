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
    
    def __str__(self):
        return self.username+"/"+self.name+"/"+self.email
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

status = (
    (0, "Order Placed"),
    (1, "Not Packed"),
    (2, "Packed"),
    (3, "Ready to Dispatch"),
    (4, "Dispatched"),
    (5, "Out for Delivery"),
    (6, "Delivered"),
    (7, "Cancelled"),
)
payment = (
    (0, "Pending"),
    (1, "Done"),
)
mode = (
    (0, "COD"),
    (1, "Net Banking"),
)
class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    orderStatus = models.IntegerField(choices=status,default=0)
    paymentMode = models.IntegerField(choices=mode,default=0)
    paymentStatus = models.IntegerField(choices=payment,default=0)
    rppid = models.CharField(max_length=50,default="",null=True,blank=True)
    totalAmount = models.IntegerField()
    shippingAmount = models.IntegerField()
    finalAmount = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.user.username
class CheckoutProducts(models.Model):
    id = models.AutoField(primary_key=True)
    checkout = models.ForeignKey(Checkout,on_delete=models.CASCADE)
    pid = models.IntegerField(default=None)#default=None (migrations k liye) means pichle jitne bhi records bane hai us coloum m pid kya dale 
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.IntegerField()
    qty = models.IntegerField()
    total = models.IntegerField()
    pic = models.CharField(max_length=50)

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(Buyer,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username +" "+ self.product.name

status=((0,'Active'),(1,'Done'))
class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    subject = models.TextField()
    message = models.TextField()
    status = models.BooleanField(choices=status,default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.email

