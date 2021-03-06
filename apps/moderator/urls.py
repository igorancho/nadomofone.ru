# coding=utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.views import logout
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .ajax import moderator_remove, moderatorinfo_update
from apps.cabinet.forms import UserChangeForm, UserAddForm
from apps.cabinet.views import UserUpdateView
from apps.moderator.views import ModeratorListView
from core.models import User

__author__ = 'alexy'

urlpatterns = patterns(
    'apps.moderator.views',
    url(r'^$', login_required(ModeratorListView.as_view()), name='list'),
    url(r'^add/$', 'moderator_add', name='add'),
    url(r'^remove/$', moderator_remove, name='remove'),
    url(r'^info/update/$', login_required(moderatorinfo_update), name='moderatorinfo'),
    url(r'^(?P<pk>\d+)/$', 'moderator_change', name='change'),
    # url(r'^user/$', staff_member_required(ListView.as_view(
    #     model=User,
    #     template_name='cabinet/user_list.html')),
    #     name='user-list'),


    # url(r'^profile/$', UserUpdateView.as_view(), name='profile'),
    # url(r'^password_change/$', 'password_change', name='password_change'),
    # url(r'^login/$', 'cabinet_login', name='login'),
    # url(r'^logout/$', logout, name='logout'),
)
