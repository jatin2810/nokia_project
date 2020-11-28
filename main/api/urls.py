from django.urls import path
from . import views

app_name='main'


urlpatterns=[
    path('list',views.ProductListView.as_view({'get':'list'}),name='product_list'),
    path('create',views.ProductCreateView.as_view(),name="product_create"),
    path('detail/',views.ProductDetailView.as_view(),name="product_detail"),
    path('delete/',views.ProductDeleteView.as_view(),name="product_delete"),
    path('update/',views.ProductUpdateView.as_view(),name="product_update"),
]