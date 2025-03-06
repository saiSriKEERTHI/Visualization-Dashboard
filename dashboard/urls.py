from django.urls import path
from .views import home, get_data  # ✅ Make sure `home` is imported correctly

urlpatterns = [
    path('', home, name='home'),  # ✅ Map root path to `home`
    path('data/', get_data, name='get_data'),
]

