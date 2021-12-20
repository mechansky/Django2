from django.urls import path
from django.views.decorators.cache import cache_page

from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', cache_page(3600)(mainapp.products), name='products'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('category/<int:pk>/<page>/', mainapp.products, name='category_page'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]

