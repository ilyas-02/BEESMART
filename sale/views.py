from rest_framework import viewsets, generics
from .serializers import ShopSerializer, SaleSerializer, LotterySerializer, PrizeSerializer
from .models import Shop, Sale, Lottery, Prize


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


class LotteryList(generics.ListCreateAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer


class LotteryDetail(generics.RetrieveAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer


class PrizeList(generics.ListCreateAPIView):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer


class PrizeDetail(generics.RetrieveAPIView):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer



# Create your views here.
