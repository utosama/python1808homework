"""day01 URL Configuration

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
from t01.views import index,my_html,get_data
from pl.views import bc,i_ht,get_kf

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^hello$",index),
    url(r"^index",my_html),
    url(r"^get_data/",get_data),
    url(r"^biancheng",bc),
    url(r"^kf",i_ht),
    url(r"^get_kfdata",get_kf)

]
