from rest_framework import serializers
from .models import Shop, Sale, Lottery, Prize


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'phone', 'email', 'website')


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'name', 'shop', 'description', 'start_date', 'end_date', 'image')


class ShopDetailSerializer(serializers.ModelSerializer):
    sales = SaleSerializer(read_only=True, many=True)

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'phone', 'email', 'website', 'sales')


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = ('id', 'name', 'lottery', 'description', 'image')


class LotterySerializer(serializers.ModelSerializer):
    prizes = PrizeSerializer(many=True, read_only=True)
    shop = ShopSerializer(read_only=True)

    class Meta:
        model = Lottery
        fields = ('id', 'name', 'shop', 'description', 'start_date', 'end_date', 'image', 'prizes')





