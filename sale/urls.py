from django.urls import path, include
from rest_framework import routers
from .views import ShopViewSet, SaleList, SaleDetail

app_name = 'sale'

router = routers.DefaultRouter()
router.register('shops', ShopViewSet)

urlpatterns = [
    path('', include(router.urls), name='shops'),
    path('sales/', SaleList.as_view(), name='sale_list'),
    path('sales/<int:pk>/', SaleDetail.as_view(), name='sale_detail'),
]