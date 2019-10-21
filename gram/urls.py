from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='gram'

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'register/',views.register,name = 'register'),
    url(r'login/',views.login_view,name='login'),
    url(r'^new/post/', views.new_post, name = 'new-post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)