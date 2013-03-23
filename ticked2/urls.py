import os.path
from django.conf.urls import patterns, include, url
from TODOs.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

stylesheets = os.path.join(os.path.dirname(__file__), 'stylesheets')

urlpatterns = patterns('',
    (r'^$', view_todos),
    (r'^todos/$', view_todos),
    (r'^todos/(\d*)/$', view_todos),
    (r'^addtodo/$', addTodoView),
    (r'^ticktodo/(\d*)/$', tickTodoView),
    (r'^unticktodo/(\d*)/$', unTickTodoView),
    (r'^tickedtodos/$', tickedTodosView),
    (r'^deletetodo/(\d*)/$', deleteTodoView),
    (r'^edittodo/(\d*)/$', editTodoView),
    (r'^stylesheets/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': stylesheets }),
    (r'^login/$', loginView),
    (r'^logout/$', logoutView),
    (r'^newuser/$', newUserView),
    (r'^createuser/$', createUserView),


    # Examples:
    # url(r'^$', 'ticked2.views.home', name='home'),
    # url(r'^ticked2/', include('ticked2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
