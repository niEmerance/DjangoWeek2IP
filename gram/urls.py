from django.conf.urls import url,include
from . import views

app_name='gram'

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'register/',views.register,name = 'register'),
    url(r'login/',views.login_view,name='login'),
]