from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import (
    home, register, user_login, custom_logout, dashboard, 
    create_post, post_list, edit_post, delete_post, post_detail, upload_profile_picture
)

urlpatterns = [
    path('home/', home, name='home'),  # ✅ Home page route
    path("dashboard/", dashboard, name="dashboard"),  # ✅ Dashboard route
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", custom_logout, name="logout"),
    path("posts/create/", create_post, name="create_post"),
    path("posts/", post_list, name="post_list"),  # 🛠 Fixed conflict with `home`
    path("posts/edit/<int:post_id>/", edit_post, name="edit_post"),
    path("posts/delete/<int:post_id>/", delete_post, name="delete_post"),
    path("__reload__/", include("django_browser_reload.urls")),
    path("posts/<int:post_id>/", post_detail, name="post_detail"),
    path('upload-profile/', upload_profile_picture, name='upload_profile'),
]

# ✅ Serve static files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
