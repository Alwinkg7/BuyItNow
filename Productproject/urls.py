from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from Productproject import settings
from django.contrib import admin
from django.urls import path, include
import product.urls, webapp.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include(product.urls)),
    path('webapp/', include(webapp.urls)),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)