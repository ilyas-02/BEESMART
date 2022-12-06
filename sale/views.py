import django_filters.rest_framework
from rest_framework import viewsets, generics, status, mixins, filters
from rest_framework.response import Response
from .serializers import ShopSerializer, SaleSerializer, LotterySerializer, PrizeSerializer, ShopDetailSerializer
from .models import Shop, Sale, Lottery, Prize


class ShopListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = []
    search_filters = ['name', 'address', 'phone', 'email']
    ordering_fields = ['address', 'name', 'phone', 'email']
    ordering = ['address', 'name']

    # def get_queryset(self):
    #     return super().get_queryset()


class ShopDetailViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer


class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['shop', 'start_date', 'end_date']


class SaleDetail(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class LotteryViewSet(viewsets.ModelViewSet):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer


class PrizeList(generics.ListCreateAPIView):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer


class PrizeDetail(generics.RetrieveAPIView):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer



# Create your views here.
