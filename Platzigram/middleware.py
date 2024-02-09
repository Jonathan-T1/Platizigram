"""Platzigram middlewere catalog."""

#DJANGO
from django.shortcuts import redirect
from django.urls import reverse

#for more information about the middlewares use this link 
#https://docs.djangoproject.com/en/4.0/topics/http/middleware/
class ProfileCompletemiddleware:
    """profile completecion Middlewere.
    
    this make us ensure that in the platform have their
    profile picture and biography.
    """
    def __init__(self, get_response):
        """Middlewere Initializacion"""
        self.get_response = get_response

    def __call__(self,request):
        """Code to be executed for each request  before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'),reverse('logout')]:
                        return redirect('update_profile')
                
        response = self.get_response(request)
        return response
