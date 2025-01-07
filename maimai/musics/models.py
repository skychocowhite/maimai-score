from django.db import models

class MusicModel(models.Model):
    name = models.CharField(max_length=1024)
    artist = models.CharField(max_length=1024)
    bpm = models.IntegerField()
    category = models.CharField(max_length=1024)
    vesion = models.CharField(max_length=1024)
    chart_designer = models.CharField(max_length=1024)
    basic_difficulty = models.FloatField()
    advanced_difficulty = models.FloatField()
    expert_difficulty = models.FloatField()
    master_difficulty = models.FloatField()
    remaster_difficulty = models.FloatField()

    pass #TODO: finish this