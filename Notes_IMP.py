# 1.Image url in background-
style="background-image: url(static/img/bg-img/bg-1.jpg);">

# 2.Image ko load karne k liye (Jinja m likhne ki jarurat nhi)
/static/ --best(new Feature add ho gya hai)
 or {% static '' %}
Ctrl+Shift+L=Multiple Selector
# 3.Select karenge text ko and ctrl+shift+L press karenge

#Models  (Table):
    # models.CASCADE :- Best Approach Agar Maincategory delete kardi to uske product automatically delete ho jayenge
    # models.ForeignKey(Maincategory,on_delete=models.RESTRICT) :-Maincategory tab tak delete nhi hogi jab tak uske product delete nhi honge
    # Protect karke rakhega

    # models.ForeignKey(Maincategory,on_delete=models.SET_NULL):-
    # Agar Maincategory ko delete kar diya to uske product m Maincategory ki jagah null value aa jayegi



myenv) PS D:\Wd 9AM Jan 2023\essence> python manage.py makemigrations
Migrations for 'mainApp':
    + Create model Brand
    + Create model Buyer
    + Create model Maincategory
    + Create model Subcategory
    + Create model Product
(myenv) PS D:\Wd 9AM Jan 2023\essence> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, mainApp, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying mainApp.0001_initial... OK
  Applying sessions.0001_initial... OK
(myenv) PS D:\Wd 9AM Jan 2023\essence> 


#Superuser admin creds
myenv) D:\Wd 9AM Jan 2023\essence>py manage.py createsuperuser
Username (leave blank to use 'vinay'): vinay
Email address: vinaymwn97@gmail.com
Password:vinay@!1234            Vinay@!1234
Password (again):vinay@!1234    Vinay@!1234


#Tables ko Register(Add) karne k liye admin.py m add karenge
from .models import * # To add all tables

  # Register your models here.
  admin.site.register(
      (
          Buyer,
          Maincategory,
          Subcategory,
          Brand,
          Product,
      )
  )
  
  Isko karne k baad admin panel par us app ka name and uski tables show ho jayegi
  
  # Mainapp---------------->
  # Brands	
  # Buyers	
  # Maincategorys	
  # Products	
  # Subcategorys	


# Image upload k liye setting.py m changes kiye
  MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
  MEDIA_URL = '/media/'

# and urls.py
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#Maincategory object 1 ko as a string dikhale k liye Male,Female,Kids
def __str__(self):
  return self.name


#Django m agar same image dobara upload karte hai to django uska change karke save kar deta hai duplicate 


#Rupay Simple k liye 
&#8377

#Filters k liye Hamne Maincategory/Subcategory/brand li hai Male,female,kids k liye 
<a href="/shop/Male/All/Alll/">Male</a>

#Mandetory field dark ho jate hai and optional light rahte hai
models.py m kuch bhi changes karenge to migrations and migrate command chalani mandatory hai



#Humne 3 types k filter lagaye hai 
1.Category wise : Maincategory,Subcategory, Brand 
2.Price wise :Minimum price and maximum price 
3.Sort Filter : Newest Item LTOH and HTOL

#31-Jan-2023
Start karni
search functionality done by size, color name description 
single-product page-00:18:50 cart page

Add to Cart -Session(Remove After set time or default time) login systemhona chahiye session k liye
Add to wishlist -DB Table

Login Start-
video-1 complete
video-2 start

Agar User login hai to -
`Logout , User Profile icon and Cart dikhega

redirect and HttpResponseRedirect m kya difference hai 
#
Buyer k sath sath user account bhi banayege
User bhi create karege jo built -in table di hai


#New Account for Buyer and User
A/C Credentials-
User Name=Trilok
Email=trilok.ranjan@gmail.com
Password=Trilok@!1234

User Name =Ankur
Email =ankurkumar07071998@gmail.com
Password=Ankur@!1234

Password direct save nhi hua:- user.set_password(password)
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



#Agar signup form m data fill aur kisi field m value nhi dali aur submit kar diya to data filled nhi rah pa raha 

Login,logout,profile page 
login page se user and admin dono kar sakte hai 
add decorator 
profile -update-pending

Start 6-Feb Video

#push code on main=Added the login,signup,logout and user profile functionality
update profile-
enctype="multipart/form-data"- image ya mmedia file lo encrypte karna padta hai

profile-update-Done 
Message bootstrap version 00:21:46

Vide0-2 Add to cart and Wishlist
Start session and cookie session 

session and cookie ki video skip hai maine project ko jaldi complete karne k iye 

#Start 08-02-2023 part-2
Add to cart/
cart/

cart page bana diya

#09-02-2022 video-1
def updateCartPage ------- 

500   5  5-1
2500    2000

cart-add to cart,display,update and delete cart ho gya 

maine bootstrap css ka link 4.1 wala lagaya hai index.html file jiski wajah se margin and padding kharab ho gya hai usko set karna hai cart and sabhi page m



#13-02-2023

#Checkout and right side bar 

video-1
12:27 

total card ki functionality laga di views m and index.html m 
card icon m  show hogi and right side m bhi dikhegi


# Checkout page start
Billing Details and Your Order and Payment mode

video-2 start

Created Checkout &Checkout product table to store the data and order the product.

status = ((0,"Order Placed"),(1,"Not Packed"),(2,"Packed"),(3,"Ready to Dispatch"),(4,"Dispatched"),(5,"Out for Delivery"),(6,"Delivered"),(7,"Cancelled"))
payment = ((0,"Pending"),(1,"Done"))
mode = ((0,"COD"),(1,"Net Banking"))
class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    orderStatus = models.IntegerField(choices=status,default=0) 0 means -> Order Placed
    paymentMode = models.CharField(choices=mode,default=0)0->COD
    paymentStatus = models.CharField(choices=payment,default=0)
    
video-1 Done table migrations and migrate

video-2 Start 
Thak You and confirmation page done

Order id ya checkout ek hi baat hai

video-3 complete

video-4 start:-
Agar checkout page par total product 0 hai to hum cart page redirect kara denge 

aur agar koi direct Checkout url ko bhi hit karega to cart page par chala jayega

Code Pushed on main branch

Start 16-02-2023 part1 :

Add to wishlist and display wishlist: 
for further purchase
agar pahle se wishlish m hai to dobara save nhi hona chahiye

Display Order History Section
#Order ka data 2 table hai 1 m checkout rakhi hai and dusre m us checkout k product
#Hame checkout and product ko ek sath use karne hai


payment = (
    (0, "Pending"),
    (1, "Done"),
)
paymentStatus=0
{{item.checkout.get_paymentStatus_display}}=Pending
isko custom templateTags se bhi kar sakte hai django documentation ki help se 20-02

M.Imp. 
Interview Question:-
Custom Template Tag kaise banate hai:-
Ans:- templatetags name ka folder banao usmi file banao use load karo
Server restart jarur karna 


Google Map Website :
Embed Google Map
website:- https://www.embedgooglemap.net/



Admin panel par tables ko database table ki tarah show karna k liye:-

# Register your models here.
admin.site.register(
    (              #yaha se us table ko hatana hoga
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