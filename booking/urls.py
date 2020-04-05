
from django.conf.urls import url
from booking import views

#app_name = 'booking'

urlpatterns = [
    url(r'^availability/$', views.availability,name ='avail'),
    url(r'^contact/$', views.contact,name ='contact'),
    url(r'^hotel/$', views.hotel,name ='hotel'),
    url(r'^$', views.home,name ='home'),
    url(r'^index_jp/$', views.index_jp,name ='index_jp'),
    url(r'^index_fr/$', views.index_fr,name ='index_fr'),
    url(r'^index_cn/$', views.index_cn,name ='index_cn'),
    url(r'^index_ar/$', views.index_ar,name ='index_ar'),
    url(r'^price/$', views.price,name ='price'),
    #url(r'^projects/$', views.projects,name ='projects'),
    url(r'^services/$', views.services,name ='services'),
    #url(r'^sidebar_right/$', views.sidebar_right,name ='sidebar_right'),
    url(r'^table/$', views.table,name ='table'),
    url(r'^search/$', views.search,name ='search'),
    url(r'^payment/$', views.payment,name ='payment'),
    url(r'^login/$', views.login,name='login'),
    url(r'^register/$', views.register,name='register'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'^profile/$', views.profile,name='profile'),
]
