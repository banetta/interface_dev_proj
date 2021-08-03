from django.contrib import admin

from .models import Product, Review, ShopBasket, MyPage

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ['p_title', 'p_image', 'p_lprice', 'p_brand', 'p_category1', 'p_category2', 'p_category3', 'p_category4']


class ReviewAdmin(admin.ModelAdmin):
    fields = ['r_title', 'r_text', 'product']


class ShopBasketAdmin(admin.ModelAdmin):
    fields = ['user', 'product', 's_ordered']


class MypageAdmin(admin.ModelAdmin):
    fields = ['user', 'product', 'm_emoney']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ShopBasket, ShopBasketAdmin)
admin.site.register(MyPage, MypageAdmin)
