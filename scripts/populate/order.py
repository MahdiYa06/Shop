import factory
from faker import Faker
from uuid import uuid4
from user.models import User
from product.models import Varient
from random import randint, choice
from order.models import Order



fake = Faker()

# -----------------------------------------------------------------------------------

class ShoppingCardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'order.ShoppingCard'
        
    user = factory.SubFactory("scripts.populate.user.UserFactory")
    
    

class ShoppingCardLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'order.ShoppingCardLine'   
        
    shopping_card = factory.SubFactory(ShoppingCardFactory)
    varient = factory.SubFactory('scripts.populate.product.VarientFactory')
    
# -----------------------------------------------------------------------------------


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'order.Order'
        
    user = factory.SubFactory("scripts.populate.user.UserFactory")
    status = factory.LazyAttribute(lambda s: choice(Order.Order_Statuses[1]))
    

class OrderLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'order.OrderLine'   
        
    order = factory.SubFactory(OrderFactory)
    varient = factory.SubFactory('scripts.populate.product.VarientFactory')
    title = factory.Faker('sentence', nb_words = 3)
    price = factory.Faker('pydecimal', positive = True ,right_digits = 2, max_value = 10000)
    
# -----------------------------------------------------------------------------------

class ShippingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'order.Shipping'
        
    order = factory.SubFactory(OrderFactory)
    address = factory.Faker('street_address')
    city = factory.Faker('city')
    postal_code = factory.Faker('postcode')
    recipient_name = factory.Faker('name')
    latitude = factory.LazyAttribute(lambda x: float(fake.latitude()))
    longitude = factory.LazyAttribute(lambda x: float(fake.longitude()))
    
    
# -----------------------------------------------------------------------------------
    
    
    

def generate_order_app_fake_data(num_shopping_card_per_user = 5):
    all_users = User.objects.all()
    all_variants = Varient.objects.all()
    
    for u in all_users:
        for _ in range(num_shopping_card_per_user):
            sh_card = ShoppingCardFactory.create(user = u)            
            selected_variant = fake.random_choices(all_variants, length=randint(0, 5))
        
            for v in selected_variant:
                ShoppingCardLineFactory.create(shopping_card = sh_card, varient = v)
                
            if randint(0, 100) < 50:
                order = OrderFactory.create(user = u)
                
                if randint(1, 100) < 80:
                    primary_address = u.primary_address
                    shipping = ShippingFactory.create(
                        order = order,
                        address = primary_address.address,
                        city = primary_address.city,
                        postal_code = primary_address.postal_code,
                        recipient_name = primary_address.recipient_name,
                        latitude = primary_address.latitude,
                        longitude = primary_address.longitude,
                    )
                else:
                    shipping = ShippingFactory.create(
                        order = order,
                    )
                    
                for v in selected_variant:
                    if randint(0, 100) < 80:
                        OrderLineFactory.create(
                            order = order,
                            varient = v,
                            title = v.title,
                            price = v.price,
                        )
                    
                    else:
                        OrderLineFactory.create(
                            order = order,
                            varient = v,
                        )
                    
                    
                    