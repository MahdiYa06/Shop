from django.db import models
from uuid import uuid4
from product.models import BaseVarient
from user.models import BaseAddress
from utils.models.base import TimeStampedModel
from django.db.models.functions import TruncDate



class ShoppingCard(TimeStampedModel):
    identifier = models.UUIDField("Unique Identifier", editable=False, default=uuid4)
    user = models.ForeignKey("user.User", verbose_name= "User", on_delete=models.SET_NULL, null=True, blank=True, related_name="shopping_cards")
    is_primary = models.BooleanField("Is this your primary shopping card ?", default=True)
    
    
    def save(self, *args, **kwargs):
        if self.is_primary is True and self.user:
            ShoppingCard.objects.filter(user = self.user).update(is_primary = False)
            
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.user} ({self.identifier})'
        
    class Meta:
        db_table = "shopping_cards"



class ShoppingCardLine(TimeStampedModel):
    shopping_card = models.ForeignKey("order.ShoppingCard", verbose_name="Shopping Card", on_delete=models.CASCADE, related_name="lines")
    varient = models.ForeignKey("product.Varient", verbose_name="Varient", on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.varient.title}'
    
    class Meta:
        db_table = "shopping_card_lines"
    
    
    
class Order(TimeStampedModel):
    ORDER_STATUS_CREATED = 'Created'
    ORDER_STATUS_CANCLE = 'Cancled'
    ORDER_STATUS_FINISHED = 'Finished'
    ORDER_STATUS_PROCCESSED = 'Proccessed'
    ORDER_STATUS_SENT = 'Sent'
    ORDER_STATUS_DELIVERED = 'Delivered'
    
    Order_Statuses = [
        (ORDER_STATUS_CREATED, 'Order Created'),
        (ORDER_STATUS_CANCLE, 'Order Cancled'),
        (ORDER_STATUS_FINISHED, 'Order Paid'),
        (ORDER_STATUS_PROCCESSED, 'Order Proccessed'),
        (ORDER_STATUS_SENT, 'Order Sent To The Delivery System'),
        (ORDER_STATUS_DELIVERED, 'Order Delivered To Customer'),
    ]
    
    user = models.ForeignKey("user.User", verbose_name= "User", on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    status = models.CharField("Order Status", max_length=50, choices=Order_Statuses)
    
    
    def __str__(self):
        return f'{self.user} -> ({self.status})'
    
    class Meta:
        db_table = "orders"
        indexes = [models.Index(TruncDate("created_at"), "created_at", name="order_created_at_date_idx")]
    
    
    
class OrderLine(BaseVarient, TimeStampedModel):
    product = None
    
    order = models.ForeignKey("order.Order", verbose_name="Order", on_delete=models.CASCADE, related_name="lines")
    varient = models.ForeignKey("product.Varient", verbose_name="Varient", on_delete=models.PROTECT, related_name="order_lines")
    
    def __str__(self):
        return f'{self.varient.title}'
    
    class Meta:
        db_table = "order_lines"
    
    
    
    
class Shipping(BaseAddress, TimeStampedModel):
    order = models.OneToOneField("order.Order", verbose_name="Order", on_delete=models.CASCADE, related_name="shipping")
    
    
    def __str__(self):
        return f'{self.recipient_name} ({self.city})'
    
    class Meta:
        db_table = "shippings"
    