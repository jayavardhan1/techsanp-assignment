from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets =(
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields':(
                    'is_student',
                    'is_faculty',
                    

                )
            }
        )
    )

admin.site.register(CustomUser,CustomUserAdmin)