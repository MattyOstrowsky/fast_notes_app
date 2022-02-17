import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.
from django.conf import settings
from django.utils import timezone


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Must have an email address")       
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)        
        user.save()
        
        return user
    
    def create_superuser(self, email, name, password=None):
        if not email:
            raise ValueError("Must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)  
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        
        return user        
        
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']
    
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    def __str__(self):
        return self.name

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.TextField(default='')
    body = models.TextField()
    date = models.DateTimeField( auto_now=True)
    notification_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.headline