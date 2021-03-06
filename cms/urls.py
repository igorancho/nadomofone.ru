# coding=utf-8
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns(
    '',
    url(r'^api_v1/', include('api.urls', namespace='api')),
    url(r'^sign/', include('apps.sign.urls', namespace='sign'),),
    url(r'^cabinet/', include('apps.cabinet.urls', namespace='cabinet'),),
    url(r'^administrator/', include('apps.administrator.urls', namespace='administrator'),),
    url(r'^superviser/', include('apps.superviser.urls', namespace='superviser'),),
    url(r'^moderator/', include('apps.moderator.urls', namespace='moderator'),),
    url(r'^city/', include('apps.city.urls', namespace='city'),),
    url(r'^client/', include('apps.client.urls', namespace='client'),),
    url(r'^adjuster/', include('apps.adjuster.urls', namespace='adjuster'),),
    url(r'^work/', include('apps.adjuster_cabinet.urls', namespace='work'),),
    url(r'^task/', include('apps.adjustertask.urls', namespace='adjustertask'),),
    url(r'^surface/', include('apps.surface.urls', namespace='surface'),),
    url(r'^ticket/', include('apps.ticket.urls', namespace='ticket'),),
    url(r'^journal/', include('apps.journal.urls', namespace='journal'),),
    url(r'^manager/', include('apps.manager.urls', namespace='manager'),),
    url(r'^incoming/', include('apps.incoming.urls', namespace='incoming'),),
    url(r'', include('core.urls')),
    url(r'', include('apps.landing.urls')),

    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
