from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import News
from .models import GalleryItem
from .forms import ContactForm
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    news_items = News.objects.order_by('-created_at')[:3]
    return render(request, 'main/home.html', {'news_items': news_items})

def news_list(request):
    news_items = News.objects.order_by('-created_at')
    return render(request, 'main/news_list.html', {'news_items': news_items})

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'main/news_detail.html', {'news': news})

def donate_view(request):
    return render(request, 'main/donate.html')

def gallery_view(request):
    items = GalleryItem.objects.order_by('-created_at')
    return render(request, 'main/gallery.html', {'items': items})

from django.contrib.auth.decorators import login_required

@login_required
def upload_gallery_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        video_url = request.POST.get('video_url') or None
        if title and image:
            GalleryItem.objects.create(title=title, image=image, video_url=video_url)
            return redirect('gallery')
    return render(request, 'main/gallery_upload.html')


from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Надіслати email адміну
            send_mail(
                subject=f"Нове повідомлення від {contact.name}",
                message=f"Email: {contact.email}\n\nПовідомлення:\n{contact.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[admin[1] for admin in settings.ADMINS],
                fail_silently=False,
            )

            messages.success(request, 'Ваше повідомлення надіслано успішно.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def home(request):
    news_items = list(News.objects.order_by('-created_at')[:3])
    return render(request, 'main/home.html', {'news_items': news_items})