from rest_framework import viewsets
from rest_framework.decorators import action

import utils.http_request.maimai_status as maimai_status
from musics.models import MusicModel
from musics.serializer import MusicSerializer
from utils.http_request.maimai_response import MaimaiResponse


class MusicModelViewSet(viewsets.ModelViewSet):
    queryset = MusicModel.objects.all()
    music_serializer = MusicSerializer

    def get_serializer_class(self):
        return self.__class__.music_serializer

    @action(methods=['GET'], detail=False)
    def hello(self, request):
        return MaimaiResponse(status_code=maimai_status.SUCCESS, data={'message': 'hello from music'})
    pass  # TODO: finish this
