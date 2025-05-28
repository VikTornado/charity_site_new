from django.contrib import admin
from .models import News
from .models import GalleryItem
from .models import ContactMessage
from ckeditor.widgets import CKEditorWidget
from django import forms

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'image']  # видалено created_at

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}  # додано автозаповнення slug

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

    

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')