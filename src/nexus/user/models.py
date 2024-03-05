from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None, **kwargs):

        if not username:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=username,
            phone_number=phone_number,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):

        user = self.create_user(
            username,
            '',
            password=password,

        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length= 30, null= True, blank= False)
    last_name = models.CharField(max_length= 30, null= True, blank= False)
    phone_number = models.CharField(max_length= 13, null= False, blank= False)
    username = models.CharField(max_length= 20, null= False, blank= False, unique= True)
    email = models.EmailField(max_length= 30, blank= True)
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default= True)
    joined_date = models.DateTimeField(auto_now_add= True, editable= False)
    update_date= models.DateTimeField(auto_now= True, editable= False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
