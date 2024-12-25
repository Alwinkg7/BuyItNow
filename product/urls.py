from django.urls import path
from product import views


urlpatterns = [
    path('addcategory/', views.addcategory, name='addcategory'),
    path('indexpage/', views.indexpage, name='indexpage'),
    path('adminloginpage/', views.adminloginpage, name='adminloginpage'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('displaycategory/', views.displaycategory, name='displaycategory'),
    path('savecategory/', views.savecategory, name='savecategory'),
    path('editcategory/<int:dataid>/', views.editcategory, name='editcategory'),
    path('deletecategory/<int:dataid>/', views.deletecategory, name='deletecategory'),
    path('updatecategory/<int:dataid>/', views.updatecategory, name='updatecategory'),
    path('productlist/', views.productlist, name='productlist'),
    path('saveproductlist/', views.saveproductlist, name='saveproductlist'),
    path('displayproductlist/', views.displayproductlist, name='displayproductlist'),
    path('editproductlist/<int:dataid>/', views.editproductlist, name='editproductlist'),
    path('deleteproductlist/<int:dataid>/', views.deleteproductlist, name='deleteproductlist'),
    path('updateproductlist/<int:dataid>/', views.updateproductlist, name='updateproductlist'),
    path('displaycontact/', views.displaycontact, name='displaycontact'),
    path('deletecontact/<int:dataid>/', views.deletecontact, name='deletecontact'),
    path('deleteuserdata/<int:dataid>/', views.deleteuserdata, name='deleteuserdata'),
    path('displayuserdata/', views.displayuserdata, name='displayuserdata'),
]
