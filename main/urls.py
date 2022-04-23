from django.urls import path
from . import views
from django.conf.urls.static import static

# spell urlpatterns in small letters
app_name = 'main'
urlpatterns = [
    path('', views.index),
    path('services.html', views.services),
    path('about.html', views.about),
    path('contact.html', views.contact),
    path('gallery.html', views.gallery),
    path('form/feedback_form.html', views.feedback_form),
    path('form/thanks.html',views.feedback_form)
]