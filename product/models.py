from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_models
from utils.models.base import TimeStampedModel



class Category(MPTTModel, TimeStampedModel):
    parent = TreeForeignKey("self", verbose_name="Category Parent", on_delete=models.PROTECT, null=True, blank=True, related_name = "childs")
    title = models.CharField("Category Title", max_length=150)
        
        
    def __str__(self) -> str:
        return  self.title + (f'({self.parent.title})' if self.parent else "")
    
    
    class MPTTModel:
        order_insertion_by = ['title']
    
    class Meta:
        db_table = "Categories"
    
    
class Product(TimeStampedModel):
    category = models.ForeignKey("product.Category", verbose_name="Product's Category", on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    title = models.CharField("Product title", max_length=254)
    description = tinymce_models.HTMLField("Product Description")
    tags = models.ManyToManyField("product.Tags", verbose_name="Product tags")
        
    def __str__(self) -> str:
        return f'{self.title} ({self.category})'
    
    class Meta:
        db_table = "Products"
        
        
        
class Tags(TimeStampedModel):
    tag = models.CharField("Product tag", max_length=50)
    
    
    def __str__(self) -> str:
        return self.tag
    
    
    
class ProductImage(TimeStampedModel):
    product = models.ForeignKey("product.Product",verbose_name="Product", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Image", upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return f'{self.product.title} ({self.id})'
    
    class Meta:
        db_table = "product_images"
    
    
    
class ProductAttribute(TimeStampedModel):
    product = models.ForeignKey("product.Product",verbose_name="Product", on_delete=models.CASCADE, related_name="attributes")
    title = models.CharField("Attribute Title", max_length=100)
    value = models.TextField("Attribute Value")
    
    def __str__(self):
        return f'{self.product} ({self.title})'
    
    class Meta:
        db_table = "product_attributes"
    

class BaseVarient(models.Model):
    product = models.ForeignKey("product.Product",verbose_name="product", on_delete=models.CASCADE, related_name="varients")
    title = models.CharField("Varient title", max_length=250)
    price = models.DecimalField("Varient price", max_digits=10, decimal_places=2)
    
    
    class Meta:
        abstract = True
        

# the last class is aleady created for some classes actually below class to abstract some fields
class Varient(BaseVarient, TimeStampedModel):
    sku = models.CharField("Varient SKU", max_length=50)
    quantity = models.IntegerField("Varient quantity", default=0)
    
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = "variants"
    
    
class ProductOption(TimeStampedModel):
    title = models.CharField("Option title", max_length=250, unique=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = "product_options"
    
    
class VarientOption(TimeStampedModel):
    varient = models.ForeignKey("product.Varient",verbose_name="Varient", on_delete=models.CASCADE, null=True, related_name="varient_options")
    option = models.ForeignKey("product.ProductOption",verbose_name="option", on_delete=models.PROTECT, db_index=False)
    value = models.CharField("Varient option value", max_length=250)
    
    def __str__(self) -> str:
        return f'{self.varient} - {self.option} - {self.value}'
    
    class Meta:
        db_table = "variant_options"