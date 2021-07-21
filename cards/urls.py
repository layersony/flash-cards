from django.urls import path
from . import views


urlpatterns = [
  path('flashcards/', views.FlashcardsAll.as_view()), # all flashcards
  path('flashcards/<int:pk>', views.FlashCardsList.as_view()), # get specific flashcard
  path('subjects/', views.SublectAll.as_view()), # get all subjects
  path('subjects/<int:pk>', views.SublectList.as_view()), # get specific one
]