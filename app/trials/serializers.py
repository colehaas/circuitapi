from rest_framework import serializers

from .models import IdentificationModule, StatusModule

class IdentificiationModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationModule
        fields = ['NCTId', 'BriefTitle', 'OfficialTitle', 'Acronym']

class StatusModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationModule
        fields = ['StatusVerifiedDate']


class Myserializer(serializers.Serializer):
    APIVrs = serializers.CharField()

