# delivery/views.py
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Restaurant, MenuItem, Order
from .serializers import RestaurantSerializer, MenuItemSerializer, OrderSerializer

def restaurents(request):
    return HttpResponse("This is the Restaurents page.")


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

