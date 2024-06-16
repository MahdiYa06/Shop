import factory
from faker import Faker
from random import randint
from product.models import Category, Varient



fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = 'product.Category'
    title = factory.sequence(lambda n: f'Category ({n})')
    parent = factory.SubFactory('scripts.populate.product.CategoryFactory')
    
    
    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'product.Product'
        
    category = factory.SubFactory(CategoryFactory)
    title = factory.Faker('sentence', nb_words = 5)
    description = factory.Faker('paragraph')
    
    
    
class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'product.ProductImage'
        
    product = factory.SubFactory(ProductFactory)
    image = factory.django.ImageField(color = factory.Faker('safe_color_name'))
    
    
    
class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'product.ProductAttribute'
        
    product = factory.SubFactory(ProductFactory)
    title = factory.Faker('word')
    value = factory.Faker('sentence')
        
        


class VarientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'product.Varient'
        
    product = factory.SubFactory(ProductFactory)
    title = factory.Faker('sentence', nb_words = 3)
    price = factory.Faker('pydecimal', positive = True ,right_digits = 2, max_value = 10000)
    sku = factory.Faker('ean', length = 13)
    quantity =  factory.Faker('random_int', min = 0, max = 100)


    
class ProductOptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'product.ProductOption'
        
    title = factory.sequence(lambda n: f'Option ({n})')
    
    
    
    
    
class VarientOptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'product.VarientOption'
        
    varient = factory.SubFactory(VarientFactory)
    option = factory.SubFactory(ProductOptionFactory)
    value = factory.Faker('word')
    
    
    
    
    
def generate_product_app_fake_data(num_root_category=3, num_products_per_categories=5, num_options = 10):
    
    options = [ProductOptionFactory.create() for _ in range(num_options)]
    
    
    root_categories = [CategoryFactory.create(parent = None) for _ in range(num_root_category)]
    for root in root_categories:
        for _ in range(randint(0, 5)):
            CategoryFactory.create(parent = root)
            
            
    all_categories = Category.objects.all()
    for category in all_categories:
        for _ in range(num_products_per_categories):
            product = ProductFactory.create(category = category)
            
            for _ in range(randint(1, 6)):
                image = ProductImageFactory.create(product = product)
                
            for _ in range(randint(1, 6)):
                attribute = ProductAttributeFactory.create(product = product)
                
            for _ in range(randint(1, 6)):
                varient = VarientFactory.create(product = product)
                
        
    variants = Varient.objects.all()
    for varient in variants:
        for option in fake.random_choices(options, length=randint(1, 6)):
            VarientOptionFactory(varient = varient, option = option)


