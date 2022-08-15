from django.urls import include, path
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="REST API (main)",
        default_version="v1.0.0",
        description="Main API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path("api/v1/", include("apps.api.v1.urls")),
    ],
)
