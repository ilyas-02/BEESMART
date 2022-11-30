from rest_framework import viewsets, generics
from .serializers import ShopSerializer, SaleSerializer
from .models import Shop, Sale


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    http_method_names = ['get', 'post', 'delete', 'head', 'options']


class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetail(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


# Create your views here.
