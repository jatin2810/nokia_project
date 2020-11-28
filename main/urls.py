from django.urls import path
from . import views


app_name='main'

urlpatterns=[
    path('',views.firstView,name='firstView'),
    path('create',views.ProductForm,name="product_create"),
    path('product_detail/<int:pk>',views.ProductDetail,name="product_detail"),
    path('product_delete/<int:pk>',views.ProductDelete,name="product_delete"),
    path('product_update/<int:pk>',views.ProductUpdate,name="product_update"),

]