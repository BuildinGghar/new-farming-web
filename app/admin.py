from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CityRegister)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4  # Set the initial number of inline fields to 5

    def get_max_num(self, request, obj=None, **kwargs):
        # Limit the number of inline fields to 5
        if obj:
            return 5 - obj.productimage_set.count()
        return self.extra

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'after_discount','price', 'product_availability', 'city', 'weight')
    list_filter = ('city', 'product_availability')
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'locality', 'city', 'state', 'zipcode')
    list_filter = ('state', 'city')
    search_fields = ('name', 'locality', 'city', 'state', 'zipcode')

admin.site.register(Customer, CustomerAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'product', 'quantity', 'total_cost')

admin.site.register(Cart, CartAdmin)



from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'paid', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id')
    search_fields = ('id', 'user__username', 'razorpay_order_id', 'razorpay_payment_id')




class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'customer', 'product', 'quantity', 'order_date', 'status', 'total_cost' ,'payment')

admin.site.register(Payment, PaymentAdmin)
admin.site.register(OrderPlaced, OrderPlacedAdmin)



@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')