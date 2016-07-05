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

from task.views import *
from blog.views import *

from blog.sec import *
from read.views import *
from img.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', img),
    url(r'^pub/$', pub),
    url(r'^show/$', show),
    url(r'^du/$', read_in_sql),
    url(r'^clear_sql/$', clear_sql),
    url(r'^series/(\d{1,4})/$', series),
    url(r'^(\d{1,4})\.html$', image),

    url(r'^blog/$', blog),
    url(r'^blog2/$', blog2),
    url(r'^blogadd/', blogadd),
    url(r'^blogde/', blogde),
    url(r'^blog/(\d*)\.html$', blogcon,name='blogcontent'),
    url(r'^blogfile/$', blogfile),

    # url(r'^about/$', About.as_view()),
    url(r'^about/$', bga),

    url(r'^read/$', read),

    url(r'^userregister/$', userregister),
    url(r'^userlogin/$', userlogin),

    url(r'^renwu/', renwu),
    url(r'^ren4/$', ren4),
    url(r'^ren4/\d{1,4}\.html$', ren4),

]
