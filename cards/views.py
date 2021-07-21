from django.shortcuts import render
from .models import Flashcard ,Subject
from rest_framework.views import APIView
from rest_framework.responses import Response
from django.http import Http404
from .serializer import FlashcardSerializer, SubjectSerializer
from permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class FlashCardsList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Flashcard.objects.get(pk=pk)
        except Flashcard.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = FlashcardSerializer(merch)
        return Response(serializers.data)

#..............
    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = FlashcardSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#..............
    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class SublectList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = SubjectSerializer(merch)
        return Response(serializers.data)

#..............
    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = SubjectSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#..............
    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
