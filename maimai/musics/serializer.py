from rest_framework import serializers

from musics.models import MusicModel


class MusicSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1024)
    artist = serializers.CharField(max_length=1024)
    bpm = serializers.IntegerField()
    category = serializers.CharField(max_length=1024)
    version = serializers.CharField(max_length=1024)
    chart_designer = serializers.CharField(max_length=1024)
    basic_difficulty = serializers.FloatField()
    advanced_difficulty = serializers.FloatField()
    expert_difficulty = serializers.FloatField()
    master_difficulty = serializers.FloatField()
    remaster_difficulty = serializers.FloatField()

    pass  # TODO: finish this
