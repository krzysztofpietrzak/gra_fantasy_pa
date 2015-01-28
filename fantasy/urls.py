from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from main.views import player_list, register_page
from main.views import login_page, index, logout_page, panel, widok_miasta
from main.views import koszary_ludzi, koszary_goblinow, uniwersytet, prorok

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fantasy.views.home', name='home'),
    # url(r'^fantasy/', include('fantasy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),

    #rejestracja
    #url(r'^register/$', 'fantasy.views.register'),

    #login
    #url(r'^login/$', 'fantasy.views.login'),

    #lista graczy
    url(r'^players/$', player_list),

    url(r'^register/$', register_page),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$',logout_page),

    url(r'^panel/$', panel),
    url(r'^widok_miasta/$', widok_miasta),

    url(r'^koszary_ludzi/',koszary_ludzi),
    url(r'^koszary_goblinow/',koszary_goblinow),

    url(r'^uniwersytet/', uniwersytet),
    url(r'^prorok/',prorok),
)