from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from bonus.views import BonusesView

urlpatterns = [
    url(r'^adm/', include('app.adm.urls', namespace="stuff")),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app.index.urls', namespace="index")),
    url(r'^menu/', include('app.menu.urls', namespace="menu")),
    url(r'^bonus/$', BonusesView.as_view(), name="bonus"),
    url(r'^deliver/$', BonusesView.as_view(), name="deliver"),
    url(r'^about/$', BonusesView.as_view(), name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
