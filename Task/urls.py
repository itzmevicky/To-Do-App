from django.urls import path
from .views import *
from . import views

urlpatterns = [
   path('update/<int:pk>',UpdateTask.as_view()),
   path('Register/',RegisterUser.as_view()),
   path('delete/<int:pk>',DeleteTask.as_view()),
   path('',Todo.as_view()),
]