"""
URL configuration for tasksdj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import re_path
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
import tasks.views as tasks_views
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view as get_schema_view_rf
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

openapi_info = openapi.Info(
      title="TasksDJ API",
      default_version='v1',
      description="TasksDJ API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="meechanic.design@gmail.com"),
      license=openapi.License(name="BSD License"),
   )
schema_view = get_schema_view(
   openapi_info,
   public=True,
   permission_classes=[permissions.AllowAny],
)

schema_view_rf = get_schema_view_rf(
    title="TasksDJ",
    description="Open API for the tasks management",
    version="1.0.0",
    public=True,
)

router = routers.DefaultRouter()
router.register(r'tasks', tasks_views.ApiTask)
router.register(r'task-tags', tasks_views.ApiTaskTag)

admin.site.site_header = 'InterDB'
admin.site.index_title = 'Administration'

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^openapi/$', schema_view_rf, name='openapi-schema'),
    re_path(r'', include(router.urls)),
]
