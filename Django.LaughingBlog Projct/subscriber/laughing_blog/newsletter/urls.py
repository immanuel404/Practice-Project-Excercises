from django.conf.urls import url
from .views import newsletter_subscribe

app_name = 'newsletter'
urlpatterns = [
url(r'^subscribe/', newsletter_subscribe, name='subscribe'),
]