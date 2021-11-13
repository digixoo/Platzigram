"""Urls users"""
# Django
from django.urls import path

# Models 
from users import views as users_views 

urlpatterns = [


    # Managment
    path('login/', users_views.login_view, name='login'),
    path('logout/', users_views.logout_view, name='logout'),
    path('signup/', users_views.signup_view, name='signup'),
    path('me/profile/', users_views.update_profile, name='update_profile'),

    # Posts
    path(
        route='<str:username>/',
        view=users_views.UserDetailView.as_view(),
        name='detail'
    ),

]
