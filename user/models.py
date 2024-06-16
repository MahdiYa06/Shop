from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from utils.models.base import TimeStampedModel



class UserManager(BaseUserManager):
    def create_user(self, phone_no, password=None, **kwargs):
        if not phone_no:
            raise ValueError("The user must have the phone number field")
        user = self.model(
            phone_no = phone_no,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_no, password=None):
        return self.create_user(phone_no, password=password, is_staff = True, is_superuser = True)




class User(AbstractUser, TimeStampedModel):
    username = None
    first_name = None
    last_name = None
    email = None
    
    phone_no = models.CharField("Phone_number", max_length=20, unique=True)
    USERNAME_FIELD = "phone_no"
    REQUIRED_FIELDS = []
    
    objects = UserManager()
        
        
    def __str__(self):
        return f'{self.phone_no}'
    
    @property
    def primary_address(self):
        try:
            return self.addresses.get(is_primary = True)
        except Address.DoesNotExist:
            return None
            
    
    class Meta:
        db_table = "users"
    



class profile(TimeStampedModel):
    user = models.OneToOneField("user.User", verbose_name='User', on_delete=models.CASCADE, related_name="profile")
    name = models.CharField('Full name', max_length=100)
    email = models.EmailField('User email', max_length=254)
    nation_no = models.CharField('Nationality number', max_length=50)
    birth_date = models.DateField("Birthday date")
    profile_pic = models.ImageField("Profile Picture", upload_to=None, height_field=None, width_field=None, max_length=None)
        
    def __str__(self) -> str:
        return f'{self.name} ({self.user.id})'
    
    class Meta:
        db_table = "profiles"
        
   
   
class BaseAddress(models.Model):
    address = models.CharField("User's address ", max_length=250)
    city = models.CharField("City", max_length=50)
    postal_code = models.CharField("Postal Code", max_length=50)
    recipient_name = models.CharField("Recipient Name", max_length=100)
    latitude = models.DecimalField("Location Latitude", max_digits=10, decimal_places=5)
    longitude = models.DecimalField("Location Longitude", max_digits=10, decimal_places=5)
    
    def __str__(self):
        return f'{self.recipient_name} ({self.city})'
    
    class Meta:
        abstract = True    
   
        
    
class Address(BaseAddress, TimeStampedModel):
    user = models.ForeignKey("user.User", verbose_name="User", on_delete=models.CASCADE, related_name="addresses")
    is_primary = models.BooleanField("Ia it your primary address?", default=False)

    
    def __str__(self) -> str:
        return f'{self.user} ({self.postal_code})'
    
    class Meta:
        db_table = "addresses"
    
    def save(self, *args, **kwargs):
        if self.id is None:
            if self.user.addresses.count() == 0:
                self.is_primary = True
        super().save(*args, **kwargs)