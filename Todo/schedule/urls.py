from django.urls import path
from .views import todo, redirect_to, read

urlpatterns = [
    path('', todo),
    path('<str:id>', redirect_to),
    path('todo/<str:title>', read)
]