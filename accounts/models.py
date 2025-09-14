from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# to create a new app use the command: python manage.py startapp category
# after creating the app you need to add it to the INSTALLED_APPS in settings.py

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name, last_name, username, email, password=None, phone_number=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        user.set_password(password)  # set_password is used to hash the password
        user.save(using=self._db)  # save the user to the database
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password, phone_number=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField(max_length=100, unique=True)
    phone_number=models.CharField(max_length=15, blank=True)

    # required fields
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD='email'  # username field is email
    REQUIRED_FIELDS=['username', 'first_name', 'last_name','phone_number'] # required fields when creating superuser

    objects=MyAccountManager()  # custom manager for the Account model

    def __str__(self):
        return self.email  # return email as string representation of the user object 
    
    def has_perm(self, perm, obj=None):
        return self.is_admin  # if user is admin then he has all permissions
    
    def has_module_perms(self, app_label):
        return True  # if user is admin then he has all permissions for any app
