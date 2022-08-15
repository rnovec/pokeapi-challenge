from django.urls import include, path

urlpatterns = [
    path(
        "v1/",
        include(("apps.api.v1.urls", "apps.api.v1"), namespace="v1"),
    ),  # noqa
]
