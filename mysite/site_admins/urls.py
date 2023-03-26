from django.urls import path, include
from .views import Home_admin_view, admin_patient_view, search_results
app_name = "site_admin"

urlpatterns = [
	path('view/',  Home_admin_view, name = "home_admin"),
	path('patient_view/', admin_patient_view, name = "admin-patient"),
	path('search/', search_results, name = "search")
]