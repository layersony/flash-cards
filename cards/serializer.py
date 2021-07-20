from rest_framework import serializers
from .models import flashcard, subject


class flashcardSerializer()
     
     class meta:
         model = projects
         fields = ['id', 'title','body','created', 'updated']

class subject()

    class meta:
        model = profile 
        fields = [ 'id', 'subject']