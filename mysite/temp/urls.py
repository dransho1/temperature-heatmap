from django.conf.urls import url

from .views import index, getdat

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/getdat', getdat, name='getdat'), # second url as API to get data from JSON
]