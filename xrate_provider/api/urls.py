from django.urls import path
from api import views_v1


urlpatterns = [
    path('v1/rates/', views_v1.rates.as_view(), name="rates"),
]