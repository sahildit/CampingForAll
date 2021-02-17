from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email Address Required")
        if not username:
            raise ValueError("Username Required")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            )

        user.is_admin = True
        user.is_staff = True
        user.is_supervisor = True
        user.save(using=self._db)
        return user



# thats what we are creating a user model
class Account(AbstractBaseUser):
    email                    = models.EmailField(verbose_name="email", max_length=60,unique=True)
    username                 = models.CharField(max_length=30,unique=True)
    date_joined              = models.DateTimeField(verbose_name='date joined',auto_now=True)
    last_login               = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin                 = models.BooleanField(default=False)
    is_staff                 = models.BooleanField(default=False)
    is_supervisor            = models.BooleanField(default=False)
    is_active                = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True