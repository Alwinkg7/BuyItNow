from django.shortcuts import render, redirect
from product.models import add_categorydb, productcategorydb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from webapp.models import contactdb, userdb
from django.contrib import messages
# Create your views here.

def indexpage(request):
    return render(request, "index.html")

def addcategory(request):
    return render(request, "add_category.html")

def savecategory(request):
    if request.method == "POST":
        na = request.POST.get('username')
        addr = request.POST.get('address')
        img = request.FILES.get('image')
        obj = add_categorydb(user_name=na, Address=addr, Picture=img)
        obj.save()
        return redirect('addcategory')

def displaycategory(request):
    data = add_categorydb.objects.all()
    return render(request, "displaycategory.html", {'data': data})

def editcategory(request,dataid):
    data = add_categorydb.objects.get(id=dataid)
    return render(request, 'edit_category.html', {'data': data})

def deletecategory(request,dataid):
    data = add_categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect('displaycategory')

def updatecategory(request, dataid):
    if request.method == "POST":
        na = request.POST.get("username")
        addr = request.POST.get("address")
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = add_categorydb.objects.get(id=dataid).Picture
        add_categorydb.objects.filter(id=dataid).update(user_name=na, Address=addr, Picture=file)
        return redirect('displaycategory')

def adminloginpage(request):
    return render(request, 'adminlog.html')

def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('name')
        password_r = request.POST.get('pass')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['name'] = username_r
                request.session['pass'] = password_r
                return redirect('indexpage')
            else:
                return redirect('adminloginpage')
        else:
            return redirect('adminloginpage')

def adminlogout(request):
    del request.session['name']
    del request.session['pass']
    return redirect('adminloginpage')

def productlist(request):
    data = add_categorydb.objects.all()
    return render(request, "add_product.html", {'data': data})

def saveproductlist(request):
    if request.method == "POST":
        categ = request.POST.get('category')
        pna = request.POST.get('pname')
        quan = request.POST.get('quantity')
        pze = request.POST.get('prize')
        desc = request.POST.get('description')
        pimg = request.FILES.get('pimage')
        obj = productcategorydb(Cname=categ, Pname=pna, Quantity=quan, Price=pze, Description=desc, Pimage=pimg)
        obj.save()
        messages.success(request, "Product has been added")
        return redirect('productlist')

def displayproductlist(request):
    data = productcategorydb.objects.all()
    return render(request, "displayproduct.html", {'data': data})

def editproductlist(request, dataid):
    data = add_categorydb.objects.all()
    products = productcategorydb.objects.get(id=dataid)
    return render(request, "edit_product.html", {'data': data, 'products': products})

def deleteproductlist(request, dataid):

    products = productcategorydb.objects.filter(id=dataid)
    products.delete()
    messages.success(request, "Product has been deleted")
    return redirect('displayproductlist')

def updateproductlist(request, dataid):
    if request.method == "POST":
        categ = request.POST.get('category')
        pna = request.POST.get('pname')
        quan = request.POST.get('quantity')
        pze = request.POST.get('prize')
        desc = request.POST.get('description')
        try:
            pimg = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(pimg.name, pimg)
        except MultiValueDictKeyError:
            file = productcategorydb.objects.get(id=dataid).Pimage
        productcategorydb.objects.filter(id=dataid).update(Cname=categ, Pname=pna, Quantity=quan, Price=pze, Description=desc, Pimage=file)
        return redirect('displayproductlist')

def displaycontact(request):
    data = contactdb.objects.all()
    return render(request, "displaycontact.html", {'data': data})

def deletecontact(request,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect('displaycontact')

def displayuserdata(request):
    data = userdb.objects.all()
    return render(request, "displayuserpage.html", {'data': data})

def deleteuserdata(request,dataid):
    data = userdb.objects.filter(id=dataid)
    data.delete()
    return redirect('displayuserdata')