from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('register/', views.registration, name='registration'),
    url('profile/', views.profile, name='profile'),
    url('search/', views.search_by_username, name='search'),
    url('post/', views.post_pic, name='post_pic')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
