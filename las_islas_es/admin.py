from django.contrib import admin
from .models import Contact, CardText, Places, Comment

# Register your models here.
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


@admin.register(CardText)
class CardText(admin.ModelAdmin):
    list_display = ('title', 'content', 'image_name')


@admin.register(Places)
class Places(admin.ModelAdmin):
    list_display = ('destinations', 'content', 'image_name')


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('comment_preview', 'user', 'created_at')

    def comment_preview(self, obj):
        preview = obj.text or ""
        return preview[:20] + ("..." if len (obj.text) > 20 else "")
    comment_preview.short_description = "Preview"