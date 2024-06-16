import factory
from faker import Faker
from order.models import Order
from uuid import uuid4
from random import choice



fake = Faker()

# -----------------------------------------------------------------------------------


SUCCRSS_STATUSES = [
        Order.ORDER_STATUS_FINISHED,
        Order.ORDER_STATUS_PROCCESSED,
        Order.ORDER_STATUS_SENT,
        Order.ORDER_STATUS_DELIVERED,
    ]


def is_payment_succeeded(obj):
    if obj.order.status in SUCCRSS_STATUSES:
        return True
    return False



class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "payment.Payment"
        
    order = factory.SubFactory('scripts.populate.order.OrderFactory')
    success = factory.LazyAttribute(is_payment_succeeded)
    tracking_id = factory.LazyAttribute(lambda n: str(uuid4()))
    status = factory.LazyAttribute(lambda s:choice(["Done", "Has'nt Done", "Pending"]))
    
    
    
def generate_payment_app_fake_data():
    '''orders = Order.objects.filter(status__in=SUCCRSS_STATUSES)
    for o in orders:
        PaymentFactory.create(order = o)'''
        
    orders = Order.objects.filter(status = Order.ORDER_STATUS_CREATED)  
    for o in orders:
        PaymentFactory.create(order = o)
    
    
     