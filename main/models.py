from django.db import models
from bs4 import BeautifulSoup
from django.utils.html import strip_spaces_between_tags
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db import models



class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Очищення HTML перед збереженням
        soup = BeautifulSoup(self.content, 'html.parser')

        # Видаляємо інлайнові стилі
        for tag in soup.find_all(True):
            tag.attrs.pop('style', None)

        # Видаляємо непотрібні &nbsp;
        cleaned_html = str(soup).replace('&nbsp;', ' ')

        # Зберігаємо оновлений контент
        self.content = strip_spaces_between_tags(cleaned_html.strip())

        # Генерація slug якщо не вказано
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

# Модель для галереї: фото, відео та дата створення
class GalleryItem(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Елемент галереї"
        verbose_name_plural = "Галерея"

        # models.py

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Повідомлення від {self.name} ({self.email})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = "Повідомлення"
        verbose_name_plural = "Зворотній зв’язок"