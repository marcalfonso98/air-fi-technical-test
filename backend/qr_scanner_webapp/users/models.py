from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone 

class CustomUserManager(BaseUserManager):
    # Normal user creation (when register new account)
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo de email debe ser establecido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Superuser creation -> needed to access Django Admin
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El usuario no tiene permiso de is_staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El usuario no tiene el permiso de is_superuser')
        
        return self.create_user(email, password, **extra_fields)

# Default user creation
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    
    username = models.CharField(max_length=150, null=True, blank=False) 

    # New users -> NOT staff
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager() 

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username'] 

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users_customuser_set', 
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users_customuser_permissions',
        blank=True,
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username or self.email