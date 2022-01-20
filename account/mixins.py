from .models import User
from django.http import Http404


class AdminUserAccess():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_panel_admin:
            return super(AdminUserAccess, self).dispatch(request, args, kwargs)
        else:
            return Http404()
