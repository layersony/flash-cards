from django.shortcuts import render
from .models import Flashcard ,Subject
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializer import FlashcardSerializer, SubjectSerializer
# from .permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class FlashcardsAll(APIView): # all flashcards
  permission_classes = (IsAuthenticated,)

  def get(self, request, format=None):
    allflashcards = Flashcard.objects.all()
    serializer = FlashcardSerializer(allflashcards, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
      serializers = FlashcardSerializer(data=request.data)
      if serializers.is_valid():
          serializers.save()
          return Response(serializers.data, status=status.HTTP_201_CREATED)
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  

class FlashCardsList(APIView): # get specific one
    permission_classes = (IsAuthenticated,)

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
class SublectList(APIView): # Get specific one
    permission_classes = (IsAuthenticated,)
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

class SublectAll(APIView): # GET ALL 
  permission_classes = (IsAuthenticated,)
  def get(self, request, format=None):
    all_merch = Subject.objects.all()
    serializers = SubjectSerializer(all_merch, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
      serializers = SubjectSerializer(data=request.data)
      if serializers.is_valid():
          serializers.save()
          return Response(serializers.data, status=status.HTTP_201_CREATED)
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)