# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from apps.incoming.data_import import client_list_import
from .views import IncomingClientListView
from .ajax import reassign_manager, get_available_manager_list, get_contact_list, get_incomingclient_info, \
    ajax_task_add, get_incomingtask_info, ajax_task_update, ajax_client_add

__author__ = 'alexy'

urlpatterns = patterns(
    'apps.incoming.views',
    url(r'^$', login_required(IncomingClientListView.as_view()), name='list'),
    url(r'^add/$', 'incomingclient_add', name='add'),
    url(r'^(?P<pk>\d+)/$', 'incomingclient_update', name='update'),
    url(r'^(?P<pk>\d+)/manager/history/$', 'incomingclientcontact_history', name='history'),
    url(r'^(?P<pk>\d+)/contact/$', 'incomingclientcontact_list', name='contact-list'),
    url(r'^(?P<pk>\d+)/contact/add/$', 'incomingclientcontact_add', name='contact-add'),
    url(r'^contact/(?P<pk>\d+)/$', 'incomingclientcontact_update', name='contact-update'),
    url(r'^task/$', 'incomingtask_list', name='task-list'),
    # url(r'^task/$', IncomingTaskListView.as_view(), name='task-list'),
    url(r'^task/add/$', 'incomingtask_add', name='task-add'),
    url(r'^task/ajax-add/$', ajax_task_add, name='ajax-task-add'),
    url(r'^ajax-client-add/$', ajax_client_add, name='ajax-client-add'),
    url(r'^task/ajax-update/$', ajax_task_update, name='ajax-task-update'),
    url(r'^task/(?P<pk>\d+)/$', 'incomingtask_update', name='task-update'),
    url(r'^reassign-manager/$', reassign_manager, name='reassign-manager'),
    url(r'^get_available_manager_list/$', get_available_manager_list, name='get_available_manager_list'),
    url(r'^get_contact_list/$', get_contact_list, name='get_contact_list'),
    url(r'^get_incomingclient_info/$', get_incomingclient_info, name='get_incomingclient_info'),
    url(r'^get_incomingtask_info/$', get_incomingtask_info, name='get_incomingtask_info'),

    url(r'^import/$', client_list_import, name='client_list_import'),

)
