from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from .UserManager import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default = uuid.uuid4, editable=False, unique=True ,max_length = 300)
    email = models.EmailField(verbose_name = 'email adress',max_length = 255, unique = True,)
    password = models.CharField(max_length= 100, verbose_name="password")
    name = models.CharField(max_length = 100)
    #dob = models.DateField(verbose_name="dob",default=None, null=None, max_length=100) #ERROR On migrations
    created_at = models.DateTimeField(verbose_name="created_at", auto_now=True) #auto now used to add just once
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now_add=True) #added each time the update
    
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False) #staff user
    is_admin = models.BooleanField(default = False) #admin
    is_superuser = models.BooleanField(default=False) #superuser

    def __str__(self):
        return self.email

    objects = UserManager()
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #email and password by default

   
        