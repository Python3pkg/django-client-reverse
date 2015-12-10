from rest_framework import serializers


class ReverserInputSerializer(serializers.Serializer):
    ident = serializers.CharField(allow_blank=False)
    args = serializers.ListField(required=False, default=None)
    kwargs = serializers.JSONField(required=False, default=None)
