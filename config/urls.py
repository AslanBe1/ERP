from django.contrib import admin
from django.urls import path, include
from config.settings import MEDIA_URL
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Everest/', include('erp.urls'),name='everest'),
    path('Everest/', include('User.urls'),name='user'),
    path('social-auth/', include('social_django.urls', namespace='social')),
] + static(MEDIA_URL, document_root=settings.MEDIA_ROOT)
