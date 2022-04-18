from django.urls import path
from . import views
from django.conf.urls.static import static

# spell urlpatterns in small letters
urlpatterns = [
    path('', views.index),
    path('services.html', views.services),
    path('about.html', views.about),
    path('contact.html', views.contact),
]