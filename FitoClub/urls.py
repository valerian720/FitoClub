"""FitoClub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#https://overcoder.net/q/685/django-admin-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D1%82%D0%B5%D0%BA%D1%81%D1%82-%D0%B7%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B0-%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-django
admin.site.site_header = 'Панель администратора' # default: "Django Administration"
admin.site.index_title = 'Изменение данных' # default: "Site administration"
admin.site.site_title = 'Администратор' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('producer.urls')),

    path('', include('django.contrib.auth.urls'))
]
