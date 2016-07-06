"""mm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from read.views import *
from web.views import *

urlpatterns = [
    url(r'^$', main),
    url(r'^forum/(\d{1,4})/$', forum),
    url(r'^forum/(\d{1,4})_(\d{1,4})/', forum),
    url(r'^(\d{1,4})\.html$', art),
    url(r'^(\d{1,4})_(\d{1,4})\.html$', art),
    url(r'^web_read/$', read_image_in_sql),
    url(r'^web_delete/$', web_delete),

    url(r'^read/$', read),

    url(r'^admin/', admin.site.urls),


]
