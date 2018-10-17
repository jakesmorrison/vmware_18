from django.conf.urls import url
from . import views

app_name = 'demo'
urlpatterns = [
    url(r'^$', views.demo, name='demo'),
    url(r'^get_data/$', views.get_data, name='get_data'),
    url(r'^start/$', views.start, name='start'),
    url(r'^shutdown/$', views.shutdown, name='shutdown'),

]