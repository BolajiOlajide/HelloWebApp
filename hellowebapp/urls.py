"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# If your new template won’t display information from your database — only simple HTML and CSS 
# then we can simplify our URL definition with a shortcut without having to add anything to views.py.
from django.views.generic import TemplateView

from collection import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	# The new URL entries we're adding:
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$', 
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^resource/(?P<slug>[-\w]+)/$', views.resource_detail, 
        name='resource_detail'),
    # new line we're adding!
    url(r'^resource/(?P<slug>[-\w]+)/edit/$', 
        views.edit_resource,
        name='edit_resource'),
    url(r'^admin/', admin.site.urls),
]
