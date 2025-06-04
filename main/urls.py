from django.urls import path
from . import views
from .views import home, news_list, news_detail, gallery_view, donate_view, contact_view  # ← додай contact_view
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),  # ← це важливо!
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('register/', views.register_view, name='register'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('donate/', views.donate_view, name='donate'),
path('gallery/', views.gallery_view, name='gallery'),
path('gallery/upload/', views.upload_gallery_item, name='upload_gallery_item'),
path('contact/', contact_view, name='contact'),  # ← оця лінія викликає помилку, якщо імпорт не зроблено
path("__reload__/", include("django_browser_reload.urls")),

]