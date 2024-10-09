from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

# This defines a namespace for the URLs in this app, meaning that all the URLs in this urlpatterns list can be
# referenced with the prefix 'core'. For example, in a Django template, you could refer to the index view
# with {% url 'core:index' %}.
app_name = 'core'

urlpatterns = [
    # An empty string '' as the URL pattern means the base URL (or root) of the app.
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]