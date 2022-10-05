from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new', views.newBook, name="new_book"),
    path('delete/<int:id>', views.deleteBook, name="delete_book"),
]