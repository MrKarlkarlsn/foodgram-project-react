from rest_framework.permissions import (BasePermission,
                                        SAFE_METHODS)


class IsAdminOrReadOnly(BasePermission):
    """
    Разрешения для администратора.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsAuthorOrAdmin(BasePermission):
    """
    Разрешения для авторов и администраторов.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return True
        return request.user and (
            request.user.is_staff or obj.author == request.user
        )
