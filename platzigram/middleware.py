# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion middleware
    
    Asegura que cada usuario que interactue con la aplicación 
    tenga su perfil completo
    """

    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Código que se ejecutará cada vez antes que la vista sea llamada"""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response