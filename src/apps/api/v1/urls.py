from django.urls import include, path

from .auth import auth_urlpatterns
from .router import router
from .swagger import schema_view

urlpatterns = [
    # authentication
    path("auth/", include(auth_urlpatterns)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include(router.urls)),
]
