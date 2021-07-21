
from rest_framework import serializers
from .models import Flashcard,Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'subject',)
class FlashcardSerializer(serializers.ModelSerializer):
    subjects= SubjectSerializer 
    class Meta:
        model = Flashcard
        fields = ('title', 'id','body', 'created', 'updated','subjects',)   