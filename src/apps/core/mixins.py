class SerializerMapMixin:
    serializer_class = NotImplemented
    action = NotImplemented
    request = NotImplemented

    def get_serializer_class(self, action=None):
        if not action:
            action = self.action
        serializer_field = f"{action}_serializer_class"
        serializer_class = getattr(self, serializer_field, self.serializer_class)
        return serializer_class


class PokeapiViewMixin:
    """
    Use this as parent class in all views. Adds:
     - ordering
     - default filtering
    """

    # Filtering
    filterset_fields = "__all__"
    ordering_fields = "__all__"
    ordering = ["-created_at"]
