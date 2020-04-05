from django.conf.urls import url
from .views import user_login
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [

    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]