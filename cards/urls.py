from django.urls import path
from . import views

urlpatterns = [
  path('flashcards/', views.FlashCardsList.as_view()),
  # path('flashcards/<int:pk>', views.FlashCardsList.as_view()),
  # path('subjects/', views.SublectList.as_view()),
  # path('subjects/<int:pk>', views.SublectList.as_view()),
]