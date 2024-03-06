from django.urls import path
from myapp.views import home, ProductDetailView

app_name='product'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
]
