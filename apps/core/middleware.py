from apps.sessions.services import get_user_from_session

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_key = request.COOKIES.get('session_key')
        request.user = get_user_from_session(session_key)
        
        response = self.get_response(request)
        return response
