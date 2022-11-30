from django.contrib import admin
from .models import Shop, Sale, Lottery, Prize


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone', 'email', 'website')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'address', 'phone')


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shop', 'start_date', 'end_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'shop__name')
    list_filter = ('start_date', 'end_date')
    ordering = ('end_date',)


class LotteryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shop', 'start_date', 'end_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'shop__name')


class PrizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lottery')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'lottery__name')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Lottery, LotteryAdmin)
admin.site.register(Prize, PrizeAdmin)

# Register your models here.
