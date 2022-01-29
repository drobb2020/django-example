from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('post/<int:id>', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faqs'),
]
