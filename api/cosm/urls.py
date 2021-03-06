"""cosm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


def reducedRegistrationRoutes():
    ignored_routes = ['login', 'logout', 'profile']
    registration_module = include('rest_registration.api.urls')
    patterns = registration_module[0].urlpatterns
    namespace = registration_module[1]

    return ([url for url in patterns if url.name not in ignored_routes], namespace)


api_urlpatterns = [
    path('accounts/', include(reducedRegistrationRoutes())),
    path('authentication/', include('authentication.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
]