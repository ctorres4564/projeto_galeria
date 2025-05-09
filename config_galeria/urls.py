# config_galeria/urls.py
from django.contrib import admin
from django.urls import path, include # 'include' já deve estar aqui
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), # Para a galeria ser a página inicial
    # Ou, se quiser um prefixo:
    # path('minha-galeria/', include('galeria.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)