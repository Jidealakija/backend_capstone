from django.urls import path
from .views import ProductHomePage, ProductDetailPage

urlpatterns = [
    path('', ProductHomePage.as_view(), name='all-products'),
    path('<str:id>/', ProductDetailPage.as_view(), name='detail'),

]
