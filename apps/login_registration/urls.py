from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index, name='my_index'),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^new_registration$', views.new_registration),
    url(r'^new$', views.new),
    url(r'^validate_login$', views.validate_login),
 
] 