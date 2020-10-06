from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from myAuth.models import MyUser


class UserAdmin(UserAdmin):
	list_display = ('email','fullname','phone', 'date_joined', 'last_login', 'is_admin','is_staff')
	fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('fullname', 'phone','photo')}),
        ('Permissions', {'fields': ('is_admin','is_staff','is_superuser','is_active')}),
    )
    
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fullnamd', 'phone', 'password1', 'password2'),
        }),
    )
	search_fields = ('email','phone',)
	readonly_fields=('date_joined', 'last_login')
	ordering = ('email',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(MyUser, UserAdmin)
