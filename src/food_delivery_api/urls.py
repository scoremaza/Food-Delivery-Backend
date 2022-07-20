from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Food Delivery API",
        default_version="v1",
        description="API endpoints for the Food Delivery API",
        contact=openapi.Contact(email="admin@enlighten-e.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    
]

admin.site.site_header = " Food Delivery API Admin"
admin.site.site_title = "Food Delivery API Admin Portal"
admin.site.index_title = "Welcome to the Food Delivery API Portal"
