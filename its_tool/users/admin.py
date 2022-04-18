from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from its_tool.users.forms import UserAdminChangeForm, UserAdminCreationForm


User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    # fieldsets = (("User", {"fields": ("",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "email", "is_superuser"]
    search_fields = ["email"]
