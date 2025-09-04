from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'email', 'cpf']
    search_fields = ['email', 'cpf',]
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Plan)
admin.site.register(UserPlan)
admin.site.register(FavoriteMovie)

