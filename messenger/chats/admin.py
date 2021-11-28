from django.contrib import admin

from .models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_filter = ('added_at',)
    list_display = ('user_id',)
