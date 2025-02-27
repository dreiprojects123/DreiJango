from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to built-in User
    bio = models.TextField(blank=True, null=True)  # Optional bio field
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Profile picture
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set creation timestamp

    def __str__(self):
        return self.user.username  # Display the username in Django Admin
    
class Post(models.Model):
    title = models.CharField(max_length=200)  # Post title
    content = models.TextField()  # Main content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when last updated
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the post
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title  # Display title in Django Admin

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Link to a post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Comment author
    text = models.TextField()  # Comment content
    timestamp = models.DateTimeField(auto_now_add=True)  # When the comment was added

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username