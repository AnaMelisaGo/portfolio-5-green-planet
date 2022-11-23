from django.contrib import admin

from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


class UserProfileInline(admin.StackedInline):
    """
    Create the userprofile inlines using the
    userprofile models and add to the user admin
    """
    model = UserProfile
    can_delete = False


class AccountsUserAdmin(AuthUserAdmin):
    """
    Add userprofile inline to the user admin
    """
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)


admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)
