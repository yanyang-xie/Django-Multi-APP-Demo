from django.conf.urls import url
from app2 import views

urlpatterns = [
    url(r'^$', views.index, name='app2_index'),
]
