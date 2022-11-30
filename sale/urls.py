from django.urls import path, include
from rest_framework import routers
from .views import ShopViewSet, SaleList, SaleDetail, LotteryList, LotteryDetail, PrizeList, PrizeDetail

app_name = 'sale'

router = routers.DefaultRouter()
router.register('shops', ShopViewSet)

urlpatterns = [
    path('', include(router.urls), name='shops'),
    path('sales/', SaleList.as_view(), name='sale_list'),
    path('sales/<int:pk>/', SaleDetail.as_view(), name='sale_detail'),
    path('lotteryes/', LotteryList.as_view(), name='lottery_list'),
    path('lotteryes/<int:pk>/', LotteryDetail.as_view(), name='lottery_detail'),
    path('prizes/', PrizeList.as_view(), name='prize_list'),
    path('prizes/<int:pk>/', PrizeDetail.as_view(), name='prize_detail'),
]