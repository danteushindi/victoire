
from django.conf.urls import url, include
from django.contrib import admin
from booking import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('booking.urls')),
    url(r'^special/',views.special,name='special'),
]
