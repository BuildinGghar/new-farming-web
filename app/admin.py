from django.contrib import admin

# Register your models here.
from .models import *
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group


admin.site.register(CityRegister)



class ProductAdmin(admin.ModelAdmin):
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
    list_display = ('id','user', 'products', 'quantity', 'total_cost')
    def products(self,obj):
        link=reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link, obj.product.name)

admin.site.register(Cart, CartAdmin)



from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'paid', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id')
    search_fields = ('id', 'user__username', 'razorpay_order_id', 'razorpay_payment_id')




class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'customers', 'products', 'quantity', 'order_date', 'status', 'total_cost' ,'payments')
    
    def products(self,obj):
        link=reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link, obj.product.name)
    def customers(self,obj):
        link=reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link, obj.customer.name)
    def payments(self,obj):
        link=reverse("admin:app_payment_change", args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>',link, obj.payment.razorpay_payment_id)
    

admin.site.register(Payment, PaymentAdmin)
admin.site.register(OrderPlaced, OrderPlacedAdmin)



@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'products')
    def products(self,obj):
        link=reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link, obj.product.name)
    
    
    
admin.site.unregister(Group)