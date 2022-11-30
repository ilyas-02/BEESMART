from rest_framework import serializers
from .models import Shop, Sale


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'phone', 'email', 'website')


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'name', 'shop', 'description', 'start_date', 'end_date', 'image')
