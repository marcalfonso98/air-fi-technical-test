
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User


# Set the Users table to save the new registered users

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email',) 
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    
    # tuple type -> ',' required to keep the logic otherwise becomes a string
    ordering = ('email',)

    # Fields when clicking on a user
    fieldsets = (
        # First box, without a name but shows both email + pwd
        (None, {'fields': ('email', 'password')}), 
        
        # Second box named "Permissions"
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Fields when clicking on "Add user+"
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
        
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )