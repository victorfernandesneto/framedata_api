from rest_framework import viewsets, generics, filters
from apps.framedata.models import Character, Move
from apps.framedata.serializer import CharacterSerializer, MoveSerializer, ListMoveCharacterSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class CharacterViewSet(viewsets.ModelViewSet):
    """showing all characters"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MoveViewSet(viewsets.ModelViewSet):
    """showing all moves"""
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['move_name']
    filterset_fields = ['character']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListCharacterMove(generics.ListAPIView):
    """listing the moves of a character"""
    def get_queryset(self):
        queryset = Move.objects.filter(character_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListMoveCharacterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['move_name']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]