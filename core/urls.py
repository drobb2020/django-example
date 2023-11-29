from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('post/<int:id>', views.post, name='post'),
    path("post_create/", views.PostCreateView.as_view(), name="post-create"),
    path("post_update/<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
    path("post_delete/<int:pk>/", views.PostDeleteView.as_view(), name="post-delete"),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faqs'),
]
