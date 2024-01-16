from django.urls import path
from .views import ProductlistAPIView

urlpatterns =[
    path('', ProductlistAPIView.as_view(), name='product-list'),
]