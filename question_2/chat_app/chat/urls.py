from django.urls import path
from .views import signup, login_view, chat_view

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('chat/<str:username>/', chat_view, name='chat'),
]