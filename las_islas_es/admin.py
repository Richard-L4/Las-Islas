from django.contrib import admin
from .models import Contact, CardText

# Register your models here.
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


@admin.register(CardText)
class CardText(admin.ModelAdmin):
    list_display = ('title', 'content', 'image_name')