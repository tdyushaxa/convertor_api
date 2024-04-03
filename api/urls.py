from django.urls import path
from . import views

urlpatterns = [
    path('pdf-to-word/',views.pdf_to_word)
]
