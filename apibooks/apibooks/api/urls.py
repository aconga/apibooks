from django.conf.urls import url
from .views import LibroCrudView, LibroAPIView

urlpatterns = [
    url(r'^$', LibroAPIView.as_view(), name='listado-libro'),
    url(r'^(?P<slug>[\w-]+)/$', LibroCrudView.as_view(), name='libro-crud')
]
