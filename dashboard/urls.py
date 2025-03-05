from django.contrib import admin
from django.urls import path, include
from .views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dashboard.urls')),
    path('', home, name='home'),  # Map root URL to home view
]

