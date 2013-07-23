from django.contrib import admin
admin.autodiscover()

from django.conf.urls import patterns, url, include
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from mysite.books import views as book_views
from mysite.contacts import views as contact_views

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       url(r'^hello/$', hello),
                       url(r'^time/$', current_datetime),
                       url(r'^time/plus/(\d{1,2})/$', hours_ahead),
                       url(r'^explorerequestmeta/$', display_meta),
                       url(r'^search/$', book_views.search),
                       url(r'^contact/$', contact_views.contact),
                       )

