from django.conf.urls import patterns, url

from todos import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^login_test$', views.test_for_login, name='test_for_login'),
    url(r'^login_sender$', views.login_sender, name='login_sender'),
    url(r'^login_accepter$', views.login_accepter, name='login_accepter'),
    url(r'^get_name$', views.get_name, name='get_name'),
)
