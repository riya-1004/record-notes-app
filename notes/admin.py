from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('content', 'owner', 'created_at')
    list_filter = ('owner',)
    ordering = ('-created_at',)
