from django.conf.urls import include, url
from . import views
from scmt import views as core_views

urlpatterns = [
    url(r'^$', views.persona_list),
    url(r'^signup/', core_views.signup, name='views.signup'),
]
