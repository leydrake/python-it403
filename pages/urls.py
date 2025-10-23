from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Login/Logout
    path('signup/', views.signup, name='signup'),  # Custom signup
]