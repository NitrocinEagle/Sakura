from django.conf.urls import url, include
from .views import LoginFormView, LogoutView, IndexView
from call_back.views import CallBackView

urlpatterns = [
    url(r'^login/$', LoginFormView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^user/', include('app.index.user.urls'), name="user"),
    url(r'^call_back/$', CallBackView, name="call_back"),
    # url(r'^sign_in/$',),
    url(r'^$', IndexView.as_view(), name="home"),
]
