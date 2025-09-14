import secrets
from django.utils import timezone
from .models import Session
from apps.users.models import User

def create_session(user: User) -> str:
    """Creates a new session for a user and returns the session key."""
    # Ensure old sessions are removed to prevent clutter
    Session.objects.filter(user=user).delete()

    session = Session.objects.create(
        user=user,
        session_key=secrets.token_hex(20)  # Generate a 40-character key
    )
    return session.session_key

def get_user_from_session(session_key: str) -> User | None:
    """Retrieves a user from a session key if it's valid and not expired."""
    if not session_key:
        return None

    try:
        session = Session.objects.select_related('user').get(session_key=session_key)
        if session.is_expired():
            session.delete()
            return None
        return session.user
    except Session.DoesNotExist:
        return None
