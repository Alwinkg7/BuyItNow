from django.contrib import messages
from django.shortcuts import render, redirect
from product.models import add_categorydb, productcategorydb
from webapp.models import contactdb, userdb, cartdb


# Create your views here.
def websitepage(request):
    data = add_categorydb.objects.all()
    return render(request, "website.html", {'data':data})

def aboutpage(request):
    return render(request, "about.html")

def productpage(request, cate):
    products = productcategorydb.objects.filter(Cname=cate)
    return render(request, "products.html", {'products':products})

def singleproduct(request, dataid):
    data = productcategorydb.objects.get(id=dataid)
    return render(request, "singleproductpage.html", {'data':data})

def savetocart(request):
    if request.method == "POST":
        Product_name = request.POST.get('productname')
        Product_price = request.POST.get('productprice')
        Product_quantity = request.POST.get('qty')
        Product_total = request.POST.get('totalprice')
        obj = cartdb(Productname=Product_name, Productprice=Product_price, Productquantity=Product_quantity, Totalprice=Product_total)
        obj.save()
        messages.success(request, "Added to cart Successfully")
        return redirect('websitepage')

def cartpage(request):
    cart = cartdb.objects.filter(User=request.session['useremail'])
    return render(request, "add_to_cart.html", {'cart':cart})

def contactpage(request):
    return render(request, "contact.html")


def savecontactlist(request):
    if request.method == "POST":
        yname = request.POST.get('Your Name')
        yemail = request.POST.get('Your Email')
        yphone = request.POST.get('Your Phone')
        ymessage = request.POST.get('Your Message')
        obj = contactdb(Yname=yname, Yemail=yemail, Yphone=yphone,Ymessage=ymessage)
        obj.save()
        return redirect('contactpage')

def userloginpage(request):
    return render(request, "userlogin.html")

def saveuserdata(request):
    if request.method == "POST":
        username = request.POST.get('user name')
        useremail = request.POST.get('user email')
        userpassword = request.POST.get('user pass')
        usercpassword = request.POST.get('user cpass')
        obj = userdb(Username=username, UserEmail=useremail, UserPassword=userpassword, UserCpassword=usercpassword)
        obj.save()
        return redirect('userloginpage')


def userlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        useremail_r = request.POST.get('useremail')
        password_r = request.POST.get('password')
        if userdb.objects.filter(UserEmail=useremail_r, UserPassword=password_r).exists():


            request.session['useremaill'] = useremail_r
            request.session['passwordl'] = password_r

            return redirect('websitepage')
        else:
            return redirect('userloginpage')

    return redirect('userloginpage')

def userlogout(request):
    del request.session['useremaill']
    del request.session['passwordl']
    return redirect('userloginpage')