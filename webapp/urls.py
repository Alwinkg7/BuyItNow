from django.urls import path
from webapp import views

urlpatterns = [
    path('websitepage/', views.websitepage, name='websitepage'),
    path('aboutpage/', views.aboutpage, name='aboutpage'),
    path('productpage/<cate>/', views.productpage, name='productpage'),
    path('singleproduct/<int:dataid>/', views.singleproduct, name='singleproduct'),
    path('savetocart/', views.savetocart, name='savetocart'),
    path('cartpage/', views.cartpage, name='cartpage'),
    path('contactpage/', views.contactpage, name='contactpage'),
    path('savecontactlist/', views.savecontactlist, name='savecontactlist'),
    path('userloginpage/', views.userloginpage, name='userloginpage'),
    path('saveuserdata/', views.saveuserdata, name='saveuserdata'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
]