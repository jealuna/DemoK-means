"""
Definition of urls for VacacionesClustering.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from rest_framework import routers
import app.forms
import app.views
from app.api import LugarViewSet

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

router = routers.DefaultRouter()
router.register('lugares', LugarViewSet)
 
urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^api/', include(router.urls)),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login$',  
            LoginView.as_view(
                template_name='app/Login.html',
                extra_context={         
                  'title': 'Login',
			      'year': datetime.now().year,
                  'site_title': 'My Site',
                  'site_header': 'My Site Login'
                  }), name='login'),
    url(r'^logout$',  
        LogoutView.as_view(
            template_name='app/logout.html',
            extra_context={         
              'next_page': '/',
              }), name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
