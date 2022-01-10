"""lostandfound URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from documents.views import*
from api.views import*
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="LOST&FOUND API",
        default_version='v1',
        description="lost and found description",
        terms_of_service="https://www.test.com/policies/terms/",
        contact=openapi.Contact(email="contact@shtrs.rw"),
        license=openapi.License(name="Test License"),
    ),
    # validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('documents.urls')),
    path('api/', include('api.urls')),
    path('useraccount/', include('useraccount.urls')),
    path('orders/', include('orders.urls')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=None), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=None), name='schema-redoc'),

]
# urlpatterns += [
#     # path('swagger-json', schema_view.without_ui(
#     #     cache_timeout=None), name='schema-json'),

# ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
