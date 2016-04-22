from django.conf.urls import url

from registry import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^houses/(?P<pk>\d+)/$', views.HouseView.as_view(),
        name='house-detail'),
]
