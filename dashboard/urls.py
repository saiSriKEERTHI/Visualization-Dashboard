from django.urls import path
from .views import home, get_data  # ✅ Fix import

urlpatterns = [
    path('', home, name='home'),  # ✅ Fix home route
    path('data/', get_data, name='get_data'),  # ✅ API data route
]
