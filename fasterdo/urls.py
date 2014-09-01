from django.conf.urls import patterns, include, url
from django.contrib import admin
from todos import urls

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fasterdo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', 'thirdauth.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todos/', include(urls)),
)
