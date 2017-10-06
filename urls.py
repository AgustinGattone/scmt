from django.conf.urls import include, url
from . import views
from django.conf.urls import handler404, handler500


urlpatterns = [
	url(r'^$', views.ingresar),
	url(r'^privado/post_list$', views.post_list, name='listado'),
	url(r'^privado/alumnos$', views.post_list_alumnos),
	url(r'^privado/profesores$', views.post_list_profesores),
	url(r'^privado/otros$', views.post_list_otros),
	url(r'^privado/archivos_alumnos$', views.archivos_alumnos),
	url(r'^privado/archivos_profesores$', views.archivos_profesores),
	url(r'^privado/archivos_otros$', views.archivos_otros),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^usuario/nuevo$', views.nuevo_usuario, name='nuevo_usuario'),
	url(r'^cerrar/$', views.cerrar),
	url(r'^privado/$', views.privado),
	url(r'^privado/tusposteos$', views.post_list_privado),
	url(r'^privado/tusposteos/post/(?P<pk>[0-9]+)/$', views.post_detail_privado),
	url(r'^chat/$', views.Chat_grupal, name='chat_grupal'),
	url(r'^post/$', views.Mensaje),
	url(r'^messages/$', views.Messages, name='messages'),
	url(r'^post_document$', views.post_document, name='post_document'),
	url(r'^subir_multimedia/$', views.model_form_upload, name='model_form_upload'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]


