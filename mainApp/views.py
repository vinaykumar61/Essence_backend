from django.shortcuts import render,redirect
from .models import * #Table se data get karne k liye 
from django.db.models import Q
def home(Request):
    data = Product.objects.all()
    data = data[::-1]
    data = data[0:10]

    brand = Brand.objects.all()

    subcategory = Subcategory.objects.all()

    return render(Request,"index.html",{'data':data,'brand':brand,'subcategory':subcategory})

def checkout(Request):
    return render(Request,"checkout.html")

def contact(Request):
    return render(Request,"contact.html")


def shop(Request,mc,sc,br):

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

def priceFilter(Request,mc,sc,br):
    
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
        return redirect("/shop/All/All/All")

    return render(Request, "shop.html", {'data': data, 'maincategory': maincategory, 'subcategory': subcategory, 'brand': brand, 'mc': mc, 'sc': sc, 'br': br,'count':count})

def sortFilter(Request,mc,sc,br):
    
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
        return redirect("/shop/All/All/All")

    return render(Request, "shop.html", {'data': data, 'maincategory': maincategory, 'subcategory': subcategory, 'brand': brand, 'mc': mc, 'sc': sc, 'br': br,'count':count})

def singleProduct(Request,num):
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
        return redirect("/shop/All/All/All")