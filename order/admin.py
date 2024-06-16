from django.contrib import admin
from order.models import ShoppingCard, ShoppingCardLine, Order, OrderLine, Shipping
from payment.models import Payment



class ShoppingCardLineInline(admin.TabularInline):
    model = ShoppingCardLine
    extra = 1
    
class ShoppingCardAdmin(admin.ModelAdmin):
    inlines = [ShoppingCardLineInline]
    
    
    
    
class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 1
    
class ShoppingInline(admin.StackedInline):
    model = Shipping
    extra = 1
class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 1
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline, ShoppingInline, PaymentInline]
    
    
    
    
admin.site.register(ShoppingCard, ShoppingCardAdmin)
admin.site.register(Order, OrderAdmin)