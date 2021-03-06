from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='gram'

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'profile/',views.profile,name='profile'),
    url(r'register/',views.register,name = 'register'),
    url(r'login/',views.login_view,name='login'),
    url(r'logout/',views.logout_view,name='logout'),
    url(r'^new/post/', views.new_post, name = 'new-post'),
    url(r'edit-profile/', views.edit_profile, name = 'edit-profile'),
    url(r'like/', views.like_post, name = 'like_post'),
    url(r'unlike/', views.unlike_post, name = 'unlike_post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)