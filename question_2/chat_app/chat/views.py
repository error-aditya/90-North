from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message
from django.contrib import messages
from django.db.models import Q  # Add this line

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Redirect to the chat view with a default username or the first user
            first_user = User.objects.exclude(id=user.id).first()  # Get the first user that is not the logged-in user
            if first_user:
                return redirect('chat', username=first_user.username)  # Redirect to chat with the first user
            else:
                return redirect('chat', username=username)  # If no other users, redirect to chat with themselves
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')

def chat_view(request, username):
    if not request.user.is_authenticated:
        return redirect('login')

    users = User.objects.exclude(id=request.user.id)
    receiver_user = User.objects.get(username=username)
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=receiver_user)) |
        (Q(sender=receiver_user) & Q(receiver=request.user))
    ).order_by('timestamp')

    return render(request, 'chat.html', {'users': users, 'messages': messages, 'receiver_user': receiver_user})