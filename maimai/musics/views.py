from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from musics.models import MusicModel
from musics.serializer import MusicSerializer


class MusicModelViewSet(viewsets.ModelViewSet):
    queryset = MusicModel.objects.all()
    music_serializer = MusicSerializer

    def get_serializer_class(self):
        return self.__class__.music_serializer

    @action(methods=['GET'], detail=False)
    def hello(self, request):
        return Response({'message': 'hello from music'})
    pass  # TODO: finish this
