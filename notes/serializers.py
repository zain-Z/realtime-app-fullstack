from rest_framework import serializers

from . import models


class NoteSerializer(serializers.ModelSerializer):
    """Convert our model (Note model) into a serializer which will return a JASON"""
    class Meta:
        model = models.Note
        fields = '__all__'
