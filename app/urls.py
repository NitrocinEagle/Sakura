from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from bonus.views import BonusesView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^', include('app.index.urls'), name="index"),
    url(r'^menu/', include('app.menu.urls'), name="menu"),
    url(r'^bonus/$', BonusesView.as_view(), name="bonus"),
    url(r'^deliver/$', BonusesView.as_view(), name="deliver"),
    url(r'^about/$', BonusesView.as_view(), name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
