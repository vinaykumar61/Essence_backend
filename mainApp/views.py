from django.shortcuts import render,HttpResponseRedirect
from .models import * #Table se data get karne k liye 
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def homePage(Request):
    data = Product.objects.all()
    data = data[::-1]
    data = data[0:10]

    brand = Brand.objects.all()

    subcategory = Subcategory.objects.all()

    return render(Request,"index.html",{'data':data,'brand':brand,'subcategory':subcategory})

@login_required(login_url="/login/")
def checkoutPage(Request):
    user = User.objects.get(username=Request.user.username)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        buyer = Buyer.objects.get(username=Request.user.username)
    total = Request.session.get("total",0)
    if(total==0):
        return HttpResponseRedirect("/cart/")
    return render(Request,"checkout.html",{'data':buyer})

@login_required(login_url="/login/")
def placeOrderPage(Request):
    user = User.objects.get(username=Request.user.username)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        total = Request.session.get("total",0)
        if(total):
            shipping = Request.session.get("shipping",0)
            final = Request.session.get('final',0)
            buyer = Buyer.objects.get(username=Request.user.username)
            #Checkout ka instance generate karenge
            checkout = Checkout()
            checkout.user = buyer
            checkout.totalAmount = total
            checkout.shippingAmount = shipping
            checkout.finalAmount = final
            checkout.save()

            cart = Request.session.get("cart")
            #None ki jarurat nhi cart m kyuki yaha tak pahuche hai to card hai kyuki card nhi hoti to tatal 0 hoti 
            for key,value in cart.items():
                checkoutProduct = CheckoutProducts()
                checkoutProduct.checkout = checkout
                checkoutProduct.pid = int(key)
                checkoutProduct.name = value['name']
                checkoutProduct.color = value['color']
                checkoutProduct.size = value['size']
                checkoutProduct.price = value['price']
                checkoutProduct.qty = value['qty']
                checkoutProduct.total = value['total']
                checkoutProduct.pic = value['pic']
                checkoutProduct.save()
            Request.session['cart']={}
            Request.session['total']=0
            Request.session['shipping']=0
            Request.session['final']=0
            Request.session['cartCount']=0
            return HttpResponseRedirect('/confirmation/')
            # (return HttpResponseRedirect('/confirmation/'))loop k bahar rahenge jitene bhi product hai sabhi ban jaye warna pahla product jo table m jayenge wahi par confirm page par chala  jayega aage nhi jayega



        else:
            #Agar total 0 hai to iska matlab card khali hai
            return HttpResponseRedirect("/cart/")

def confirmationPage(Request):
    return render(Request,"confirmation.html")

def contactPage(Request):
    if (Request.method=="POST"):
        c = ContactUs()
        c.name = Request.POST.get('name')
        c.email = Request.POST.get('email')
        c.phone = Request.POST.get('phone')
        c.subject = Request.POST.get('subject')
        c.message = Request.POST.get('message')
        c.save()
        messages.success(Request,"Thanks to Share Your Query With Us.Our Team Will Contact Soon...")
        return HttpResponseRedirect('/contact/')
    return render(Request,"contact.html")

def shopPage(Request,mc,sc,br):

    if mc=="All" and sc=="All" and br=="All":
        data = Product.objects.all()
    elif mc!="All" and sc=="All" and br=="All":
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc))
    elif mc=="All" and sc!="All" and br=="All":
        data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc))
    elif mc=="All" and sc=="All" and br!="All":
        data = Product.objects.filter(brand=Brand.objects.get(name=br))
    #Double and condtion eg:- where maincategory and subcategory , and ka kaam kar raha hai 
    elif mc != "All" and sc != "All" and br == "All":
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc))
    elif mc != "All" and sc == "All" and br != "All":
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), brand=Brand.objects.get(name=br))
    elif mc == "All" and sc != "All" and br != "All":
        data = Product.objects.filter(brand=Brand.objects.get(name=br), subcategory=Subcategory.objects.get(name=sc))
    else:
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), brand=Brand.objects.get(name=br), subcategory=Subcategory.objects.get(name=sc))
    
    count = len(data)
    data = data[::-1]
    maincategory = Maincategory.objects.all()
    subcategory = Subcategory.objects.all()
    brand = Brand.objects.all()

    return render(Request, "shop.html", {'data': data, 'maincategory': maincategory, 'subcategory': subcategory, 'brand': brand, 'mc': mc, 'sc': sc, 'br': br,'count':count})

def priceFilterPage(Request,mc,sc,br):
    
    if (Request.method=="POST"):
        min = Request.POST.get("min")
        max = Request.POST.get("max")

        if mc=="All" and sc=="All" and br=="All":
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max)
        elif mc!="All" and sc=="All" and br=="All":
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,maincategory=Maincategory.objects.get(name=mc))
        elif mc=="All" and sc!="All" and br=="All":
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,subcategory=Subcategory.objects.get(name=sc))
        elif mc=="All" and sc=="All" and br!="All":
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,brand=Brand.objects.get(name=br))
        elif mc != "All" and sc != "All" and br == "All":
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc))
        elif mc != "All" and sc == "All" and br != "All":
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,maincategory=Maincategory.objects.get(name=mc), brand=Brand.objects.get(name=br))
        elif mc == "All" and sc != "All" and br != "All":
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,brand=Brand.objects.get(name=br), subcategory=Subcategory.objects.get(name=sc))
        else:
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,maincategory=Maincategory.objects.get(name=mc), brand=Brand.objects.get(name=br), subcategory=Subcategory.objects.get(name=sc))

        # data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max)
        count = len(data)
        data = data[::-1]    #Jo sabse baad m add hua usko pahle dikhale k liye
        maincategory = Maincategory.objects.all()
        subcategory = Subcategory.objects.all()
        brand = Brand.objects.all()
    else:
        return HttpResponseRedirect("/shop/All/All/All")

    return render(Request, "shop.html", {'data': data, 'maincategory': maincategory, 'subcategory': subcategory, 'brand': brand, 'mc': mc, 'sc': sc, 'br': br,'count':count})

def sortFilterPage(Request,mc,sc,br):
    
    if (Request.method=="POST"):
        sort = Request.POST.get("sort")
        if(sort =="Newest"):
            sort="id" #+ve value decending
        elif(sort=="LTOH"):
            sort="-finalprice" #-ve value ascending
        else:
            sort="finalprice"
        if mc=="All" and sc=="All" and br=="All":
            data = Product.objects.all().order_by(sort)
        elif mc!="All" and sc=="All" and br=="All":
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by(sort)
        elif mc=="All" and sc!="All" and br=="All":
            data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by(sort)
        elif mc=="All" and sc=="All" and br!="All":
            data = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by(sort)
        elif mc != "All" and sc != "All" and br == "All":
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), subcategory=Subcategory.objects.get(name=sc)).order_by(sort)
        elif mc != "All" and sc == "All" and br != "All":
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), brand=Brand.objects.get(name=br)).order_by(sort)
        elif mc == "All" and sc != "All" and br != "All":
            data = Product.objects.filter(brand=Brand.objects.get(name=br), subcategory=Subcategory.objects.get(name=sc)).order_by(sort)
        else:
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc), brand=Brand.objects.get(name=br), subcategory=Subcategory.objects.get(name=sc)).order_by(sort)

        # data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max)
        count = len(data)
        data = data[::-1]    #Jo sabse baad m add hua usko pahle dikhale k liye
        maincategory = Maincategory.objects.all()
        subcategory = Subcategory.objects.all()
        brand = Brand.objects.all()
    else:
        return HttpResponseRedirect("/shop/All/All/All")

    return render(Request, "shop.html", {'data': data, 'maincategory': maincategory, 'subcategory': subcategory, 'brand': brand, 'mc': mc, 'sc': sc, 'br': br,'count':count})

def singleProductPage(Request,num):
    data = Product.objects.get(id=num)
    return render(Request,"single-product.html",{'data':data})

def searchPage(Request):
    if(Request.method=='POST'):
        search = Request.POST.get('search')
        data = Product.objects.filter(Q(name__icontains=search)|Q(color__icontains=search)|Q(size__icontains=search)|Q(description__icontains=search))#i means case insensitive and contains same se like in sql

        count = len(data)
        maincategory = Maincategory.objects.all()
        subcategory = Subcategory.objects.all()
        brand = Brand.objects.all()

        return render(Request, "shop.html", {'data': data, 'maincategory': maincategory, 'subcategory': subcategory, 'brand': brand, 'mc': 'All', 'sc': 'All', 'br': 'All','count':count})

    else:
        return HttpResponseRedirect("/shop/All/All/All")

def loginPage(Request):
    if (Request.method=="POST"):
        username = Request.POST.get('username')
        password = Request.POST.get('password')

        # Check if any field is blank
        if not all([username, password]):
            print("2222222222222")
            print(Request.POST)
            messages.error(Request, "Please fill all fields!")
            return HttpResponseRedirect("/login/")
            # return render(Request,"login.html")


        user = authenticate(username=username,password=password)
        if user is not None:
            login(Request,user)
            if (user.is_superuser):
                return HttpResponseRedirect('/admin')
            else:
                return HttpResponseRedirect('/profile')
        else:
            messages.error(Request,"Invalid Username or Password...")
    return render(Request,"login.html")

def signupPage(Request):
    if (Request.method=="POST"):
        # print(Request.POST)
        name = Request.POST.get('fullname')
        username = Request.POST.get('username')
        email = Request.POST.get('email')
        phone = Request.POST.get('phone')
        password = Request.POST.get('password')
        cpassword = Request.POST.get('cpassword')

        # Check if any field is blank
        if not all([name, username, email, phone, password, cpassword]):
            print("111111111111111111")
            print(Request.POST)
            messages.error(Request, "Please fill all fields!")
            return HttpResponseRedirect("/signup/")
            # return render(Request,"signup.html")

        if (password == cpassword):
            try:
                user = User(username=username)
                user.set_password(password)
                user.save()
                buyer = Buyer()
                buyer.name = name
                buyer.username = username
                buyer.email = email
                buyer.phone = phone
                buyer.password = password
                buyer.save()
                return HttpResponseRedirect('/login')

            except:
                    messages.error(Request,"User Name Already Exist!!!")
        else:
            messages.error(Request,"Password and Confirm Password does'nt matched!!!")

    return render(Request,"signup.html")

def logoutPage(Request):
    logout(Request)
    return HttpResponseRedirect('/login/')

@login_required(login_url="/login/")
def profilePage(Request):
    user = User.objects.get(username=Request.user.username)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        buyer = Buyer.objects.get(username=Request.user.username)
        wishlist = Wishlist.objects.filter(user=buyer)
        #Order History
        orders = []
        checkouts = Checkout.objects.filter(user=buyer)
        for item in checkouts:
            cp = CheckoutProducts.objects.filter(checkout=item)
            data = {
                'checkout':item,
                'checkoutProduct':cp
            }
            orders.append(data)
        # print(orders)
    return render(Request,'profile.html',{'data':buyer,'wishlist':wishlist,'orders':orders})

@login_required(login_url="/login/")
def updateProfilePage(Request):
    user = User.objects.get(username=Request.user.username)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        buyer = Buyer.objects.get(username=Request.user.username)
        if(Request.method=="POST"):
            buyer.name = Request.POST.get("fullname")
            buyer.email = Request.POST.get("email")
            buyer.phone = Request.POST.get("phone")
            buyer.addressline1 = Request.POST.get("addressline1")
            buyer.addressline2 = Request.POST.get("addressline2")
            buyer.addressline3 = Request.POST.get("addressline3")
            buyer.pin = Request.POST.get("pin")
            buyer.city = Request.POST.get("city")
            buyer.state = Request.POST.get("state")
            if (Request.FILES.get("pic")):
                buyer.pic = Request.FILES.get("pic")
            buyer.save()
            return HttpResponseRedirect("/profile")
    return render(Request,"update-profile.html",{'data':buyer})

def addToCartPage(Request,num):
    p = Product.objects.get(id=num)
    cart = Request.session.get("cart",None)
    cartCount = Request.session.get("cartCount",0)
    if(cart):
        if(str(p.id) in cart):
            item = cart[str(p.id)]
            item['qty']=item['qty']+1
            item['total']=item['total']+p.finalprice
            cart[str(p.id)]=item
        else:
            cart.setdefault(str(p.id),{'name':p.name,'color':p.color,'size':p.size,'price':p.finalprice,'qty':1,'total':p.finalprice,'pic':p.pic1.url})
    else:
        cart = {str(p.id):{'name':p.name,'color':p.color,'size':p.size,'price':p.finalprice,'qty':1,'total':p.finalprice,'pic':p.pic1.url}}
    Request.session['cart']=cart
    total = 0
    for value in cart.values():
        total = total+value['total']
    if(total<1000 and total>0):
        shipping = 150
    else:
        shipping = 0
    Request.session['total']=total
    Request.session['shipping']=shipping
    Request.session['final']=total+shipping
    Request.session['cartCount']=cartCount+1
    return HttpResponseRedirect("/cart/")



def cartPage(Request):
    cart = Request.session.get('cart',None)
    items = []
    if(cart):
        for key,value in cart.items():
            value.setdefault('id',key)
            items.append(value)
    total = Request.session.get('total',0)
    shipping = Request.session.get('shipping',0)
    final = Request.session.get('final',0)
    return render(Request,"cart.html",{'cart':items,'total':total,'shipping':shipping,'final':final})

def deleteCartPage(Request,id):
    cart = Request.session.get("cart",None)
    cartCount = 0
    if(cart and id in cart):
        del cart[id]
        Request.session['cart']=cart

        total = 0
        for value in cart.values():
            total = total+value['total']
            cartCount = cartCount+value['qty']
        if(total<1000 and total>0):
            shipping = 150
        else:
            shipping = 0
        Request.session['total']=total
        Request.session['shipping']=shipping
        Request.session['final']=total+shipping
        Request.session['cartCount']=cartCount
    return HttpResponseRedirect("/cart/")


def updateCartPage(Request,id,op):
    cart = Request.session.get("cart",None)
    cartCount = Request.session.get("cartCount",0)
    if(cart and id in cart):
        item = cart[id]
        if(op=="dec" and item['qty']==1):
            pass
        elif(op=="dec"):
            item['qty']=item['qty']-1
            item['total']=item['total']-item['price']
            cartCount=cartCount-1  
        else:
            item['qty']=item['qty']+1
            item['total']=item['total']+item['price']
            cartCount=cartCount+1
        cart[id]=item 
        Request.session['cart']=cart
        Request.session['cartCount']=cartCount

        total = 0
        for value in cart.values():
            total = total+value['total']
        if(total<1000 and total>0):
            shipping = 150
        else:
            shipping = 0
        Request.session['total']=total
        Request.session['shipping']=shipping
        Request.session['final']=total+shipping
        
    return HttpResponseRedirect("/cart/")

@login_required(login_url="/login/")
def addToWishlistPage(Request,num):
    user = User.objects.get(username=Request.user.username)
    if(user.is_superuser):
        return HttpResponseRedirect("/admin/")
    else:
        buyer = Buyer.objects.get(username=Request.user.username)
        product = Product.objects.get(id=num)
        try:
            wishlist = Wishlist.objects.get(user=buyer,product=product)
        except:
            wish = Wishlist()
            wish.user = buyer
            wish.product = product
            wish.save()
        return HttpResponseRedirect("/profile/")

@login_required(login_url="/login/")
def deleteWishlistPage(Request,num):
    user = User.objects.get(username=Request.user.username)
    if(user.is_superuser):
        return HttpResponseRedirect("/admin/")
    else:
        buyer = Buyer.objects.get(username=Request.user.username)
        product = Product.objects.get(id=num)
        try:
            wishlist = Wishlist.objects.get(user=buyer,id=num)
            wishlist.delete()
        except:
            pass
        return HttpResponseRedirect("/profile/")