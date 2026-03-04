from django.urls import path
from . import views

urlpatterns = [
    path('motamagebi/', views.motamagebis_sia, name='motamagebis_sia'),
    path('motamagebi/<int:pk>/', views.motamage_detail, name='motamage_detail'),
    path('motamagebi/<int:pk>/washla/', views.motamage_washla, name='motamage_washla'),
]
