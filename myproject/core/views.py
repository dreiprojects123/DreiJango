from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm, ProfilePictureForm
from .models import Post, Profile
from django.shortcuts import get_object_or_404

# Home Page View
def home(request):
    posts = Post.objects.all().order_by('-created_at')  
    
    user_posts = Post.objects.filter(author=request.user).order_by('-created_at') if request.user.is_authenticated else None  # Fetch only user's posts

    return render(request, "core/home.html", {
        "posts": posts,
        "user_posts": user_posts  
    })
    
def user_login(request): 
    if request.method == "POST":
        username = request.POST.get("username") 
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user) 
            messages.success(request, "Login successful. Welcome back!")
            return redirect("home") 
        else:
            messages.error(request, "Invalid username or password.") 
            return redirect("login") 

    return render(request, "core/login.html")

# Register View
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")  
        else:
            messages.error(request, "Registration failed. Please check your details.")

    else:
        form = CustomUserCreationForm()
    
    return render(request, "core/register.html", {"form": form})

# Logout View
def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")  

# Protected Dashboard View (Requires Login)
@login_required
def dashboard(request):
    return render(request, "core/dashboard.html")

@login_required
def create_post(request):
    if request.method == "POST":
        
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign the logged-in user as the author
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("post_list")  # Redirect to post list view
    else:
        form = PostForm()
    
    return render(request, "core/create_post.html", {"form": form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Show latest posts first
    return render(request, "core/post_list.html", {"posts": posts})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect("post_list")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect("post_list")
    else:
        form = PostForm(instance=post)
    
    return render(request, "core/edit_post.html", {"form": form, "post": post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect("post_list")

    post.delete()
    messages.success(request, "Post deleted successfully!")
    return redirect("post_list")

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "core/post_detail.html", {"post": post})

@login_required
def upload_profile_picture(request):
    # ✅ Ensure the user has a profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # ✅ Redirect back to home page

    return redirect('home')