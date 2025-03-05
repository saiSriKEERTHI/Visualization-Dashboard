from django.contrib import admin
from django.urls import path, include
from dashboard.views import home  # ✅ Import `home` from `dashboard.views`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dashboard.urls')),  # Include dashboard app's URLs
    path('', home, name='home'),  # Redirect root URL to home API response
]
