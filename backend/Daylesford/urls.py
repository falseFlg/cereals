"""Daylesford URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import os

from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.urls import path, include, re_path
from django.views.static import serve


def serve_docs(request, path):
    return serve(request, path, document_root=settings.DOCS_DIR)


docs_urlpatterns = [
    re_path(r"^(?P<path>.*)$", serve_docs),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("info/", include(docs_urlpatterns)),
    path("", include("main.urls")),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
