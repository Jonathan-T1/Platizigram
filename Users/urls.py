"""Users Urls."""

# Django
from django.urls import path


# Views
from Users import views

urlpatterns = [

    # Managment
    path(
        route='login/',
        view=views.login_view,
        name='login'
        ),
    path(
        route='logout/',
        view=views.logout_view, 
        name='logout'
        ),
    path(
        route='signup/',
        view=views.signup_view, 
        name='signup'
        ),
    path(
        route='my/profile/',
        view=views.update_profile, 
        name='update'
        ),

    # Posts
    path(
        route='<str:user>/',
        view=views.UserDatailview.as_view(),
        name='detail',
    ),
]
