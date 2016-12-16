from django.conf.urls import url
from temp.views import HomeView

#from .views import index, getdat, ktdata

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    #url(r'^api/getdat', getdat, name='getdat'), # second url as API to get data from JSON
    #url(r'^api/ktdata', ktdata, name = 'ktdata'),
]