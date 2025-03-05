from django.urls import path
from .views import home, get_data  # ✅ Make sure 'home' is imported

urlpatterns = [
    path('', home, name='home'),  # ✅ Root API response
    path('data/', get_data, name='get_data'),  # ✅ Endpoint for fetching data
]

