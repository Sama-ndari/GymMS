from django.contrib.auth.hashers import check_password
from .models import User

def authenticate_user(email: str, password: str) -> User | None:
    """Authenticates a user by email and password."""
    try:
        user = User.objects.get(email=email)
        if user.check_password(password) and user.is_active:
            return user
    except User.DoesNotExist:
        return None
    return None
