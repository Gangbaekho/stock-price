from rest_framework import serializers

class DoomoolmoriSerializer(serializers.Serializer):
    ticker = serializers.CharField()
    date_from = serializers.DateField()
    date_to = serializers.DateField()
    