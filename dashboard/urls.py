from django.urls import path
from .views import home, get_data  # ✅ Import both views

urlpatterns = [
    path('', home, name='home'),  # ✅ Home endpoint
    path('data/', get_data, name='get_data'),  # ✅ Data endpoint
]

