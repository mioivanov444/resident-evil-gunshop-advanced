from django.contrib.auth.mixins import UserPassesTestMixin

class ModeratorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        # Allow if user is staff OR in the 'moderator' group
        return user.is_staff or user.groups.filter(name='Moderator').exists()

    def handle_no_permission(self):
        # Optional: redirect to login if not authenticated
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        # Otherwise show 403 page
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied