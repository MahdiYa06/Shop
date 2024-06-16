from django.db import models
from utils.models.base import TimeStampedModel
from django.db.models.functions import TruncDate



class Payment(TimeStampedModel):
    order = models.ForeignKey("order.Order", verbose_name="Order", on_delete=models.PROTECT, related_name="payments")
    success = models.BooleanField("succeeded")
    tracking_id = models.CharField("Payment Gateway Tracking ID", max_length=150)
    status = models.CharField("Order Status", max_length=150)
    
    def __str__(self):
        return f'{self.order}-({self.success})'
    
    class Meta:
        db_table = "payments"
        indexes = [models.Index(TruncDate("created_at"), "created_at", name="payment_created_at_date_idx")]
    
