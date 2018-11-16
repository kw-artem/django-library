from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.note_list),
    path('notes/<int:id>/', views.note_detail),
]
