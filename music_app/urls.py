from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'music_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    #path('signup/',views.signup,name='signup'),
    #path('user_login/',views.user_login,name='user_login'),
]

