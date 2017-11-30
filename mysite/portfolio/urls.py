from django.conf.urls import url

from . import views


urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # Projects Page
    url(r'^projects/$', views.projects, name='projects'),

    # Contact Page
    url(r'^contact/$', views.email, name='email'),

]
