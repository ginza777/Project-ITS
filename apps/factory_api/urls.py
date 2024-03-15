from django.urls import path
from .views import GetProduct,GetProductList

urlpatterns = [
    path('products/list', GetProductList.as_view(), name='get_product_list'),
    path('products/', GetProduct.as_view(), name='get_product'),

]
