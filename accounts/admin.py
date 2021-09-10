from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm, UserGroupForm


User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    update_form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    group_form = UserGroupForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin',)
    list_filter = ('admin', 'staff',)
    fieldsets = (
        (None, {'fields': ('image','email', 'first_name', 'last_name','phone1','phone2','gender','password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin','staff','active', 'group','is_a_driver', 'is_car_owner')}),
        # ('Groups', {'fields': ('name')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)


# class UserAdmin(admin.ModelAdmin):
#     search_fields = ['email']
#     add_form = UserAdminCreationForm # create view
#     update_form = UserAdminChangeForm # update view
#     # class Meta:
#     #     model = User

# admin.site.register(User, UserAdmin)
# admin.site.register(GuestEmail)