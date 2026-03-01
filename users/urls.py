from django.urls import path
from . import views

urlpatterns = [
    # ყველა მომხმარებელი
    path('motamagebi/', views.motamagebis_sia, name='motamagebis_sia'),
    # კონკრეტული მომხმარებელი
    path('motamagebi/<int:pk>/', views.motamage_detail, name='motamage_detail'),
    # წაშლა
    path('motamagebi/<int:pk>/washla/', views.motamage_washla, name='motamage_washla'),
]
