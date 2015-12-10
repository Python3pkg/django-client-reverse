from rest_framework import serializers


class ReverserInputSerializer(serializers.Serializer):
    ident = serializers.CharField(allow_blank=False)
