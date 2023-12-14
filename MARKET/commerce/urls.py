from django.urls import path
from .views import ProductHomePage, ProductDetailPage,CreateCartPage, ItemsListPage, AddToCartPage

urlpatterns = [
    path('products/', ProductHomePage.as_view(), name='all-products'),
    path('cart/', CreateCartPage.as_view(), name='cart'),
    path('cartitems/', ItemsListPage.as_view(), name='cart_items'),
    path('<uuid:id>/addtocart/', AddToCartPage.as_view(), name='cart_add'),
    path('<str:id>/', ProductDetailPage.as_view(), name='detail'),
]
