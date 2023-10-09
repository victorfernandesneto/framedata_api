from rest_framework import viewsets, generics, filters
from django.shortcuts import redirect, render
from apps.framedata.models import Character, Move
from apps.framedata.serializer import CharacterSerializer, MoveSerializer, ListMoveCharacterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from insert_data import insert_data

class CharacterViewSet(viewsets.ModelViewSet):
    """showing all characters"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    # @method_decorator(cache_page(2629800))
    # def dispatch(self, *args, **kwargs):
    #     return super(CharacterViewSet, self).dispatch(*args, **kwargs)

class MoveViewSet(viewsets.ModelViewSet):
    """showing all moves"""
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['move_name']
    filterset_fields = ['character']
    
    # @method_decorator(cache_page(2629800))
    # def dispatch(self, *args, **kwargs):
    #     return super(MoveViewSet, self).dispatch(*args, **kwargs)

class ListCharacterMove(generics.ListAPIView):
    """listing the moves of a character"""
    def get_queryset(self):
        queryset = Move.objects.filter(character_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListMoveCharacterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['move_name']

    # @method_decorator(cache_page(2629800))
    # def dispatch(self, *args, **kwargs):
    #     return super(ListCharacterMove, self).dispatch(*args, **kwargs)