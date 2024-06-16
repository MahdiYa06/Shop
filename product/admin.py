from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from product.models import Category, Product, ProductImage, ProductAttribute, Varient, VarientOption, ProductOption, Tags



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
       
class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1
    
class ProductVarientInline(admin.TabularInline):
    model = Varient
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductAttributeInline, ProductVarientInline]
    
    
    
    
    
    
    
class VarientOptionsInline(admin.TabularInline):
    model = VarientOption
    extra = 1
    
class VarientAdmin(admin.ModelAdmin):
    inlines = [VarientOptionsInline]
    





admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Varient, VarientAdmin)
admin.site.register(ProductOption)
admin.site.register(Tags)