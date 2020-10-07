from django.db import models
import uuid

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, fullname, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not fullname:
            raise ValueError('Users must have a name')
        if not phone:
            raise ValueError('Users must have a number')

        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, phone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            fullname=fullname,
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    fullname = models.CharField(max_length=60)
    phone = models.PositiveIntegerField()
    photo = models.ImageField()
    is_artisan = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'phone']

    objects = MyUserManager()

    def __str__(self):
        return self.fullname

    def get_name(self):
        name = self.fullname.split(" ")[1]
        return name

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
