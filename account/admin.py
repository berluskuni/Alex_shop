# coding: utf8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.forms import CreationFormUser
from account.forms import UserChangeForm
from account.models import User


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = CreationFormUser

    list_display = [
        'first_name',
        'last_name',
        'email',
        'address',
        'phone',
        'post_code',
        'city',
        'country_id',

    ]
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'avatar',
                'first_name',
                'last_name',
                'address',
                'phone',
                'post_code',
                'city',
                'country_id',


            )}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2'
            )
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
