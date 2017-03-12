from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  BankDataViewSet, DetailsView
from bloodbank_api import views

router = routers.DefaultRouter()

router.register(r'details', BankDataViewSet)

'''urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] '''

urlpatterns = [
    url(r'users/$', DetailsView.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', views.change_details),
    url(r'users', views.query_users),


]

urlpatterns = format_suffix_patterns(urlpatterns)