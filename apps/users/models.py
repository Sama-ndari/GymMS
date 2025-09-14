from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import BaseUserManager
from core.enums import UserRole

class UserManager(BaseUserManager):
    def create_user(self, email, password, nom, role=UserRole.CLIENT):
        """Create and return a User with an email and password."""
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            nom=nom,
            role=role,
            is_active=False  # All users start inactive
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, nom):
        """Create and return a superuser with an email and password."""
        user = self.create_user(
            email=email,
            password=password,
            nom=nom,
            role=UserRole.ADMIN
        )
        user.is_active = True  # Superusers are active by default
        user.save()
        return user

class User(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.CLIENT)
    date_creation = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)  # Users need admin activation

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom']

    def __str__(self):
        return f"{self.nom} ({self.email})"

    def set_password(self, raw_password):
        """Hash and set the password."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Check if the provided password matches the stored password."""
        return check_password(raw_password, self.password)

    def has_perm(self, perm, obj=None):
        """Return True if user has the specified permission."""
        return self.role == UserRole.ADMIN

    def has_module_perms(self, app_label):
        """Return True if user has permissions to view the app."""
        return self.role == UserRole.ADMIN

    @property
    def is_staff(self):
        """Return True if user is admin."""
        return self.role == UserRole.ADMIN

    @property
    def is_superuser(self):
        """Return True if user is admin."""
        return self.role == UserRole.ADMIN

    class Meta:
        app_label = 'users'
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ['nom']
