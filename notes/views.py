from django.shortcuts import render
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer
from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote
# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getNotes(request):

    if request.method == 'GET':
        return getNotesList(request)

    if request.method == 'POST':
        return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getNote(request, pk):

    if request.method == 'GET':
        return getNoteDetail(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)

    if request.method == 'DELETE':
        return deleteNote(request, pk)
