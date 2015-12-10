from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.core.urlresolvers import reverse, NoReverseMatch
from .serializers import ReverserInputSerializer


class Reverser(APIView):
    renderer_classes = (JSONRenderer,)

    def post(self, request, format=None):
        input_serializer = ReverserInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        try:
            url = reverse(input_serializer.validated_data['ident'])
        except NoReverseMatch:
            return Response(status=404)
        return Response(url, 302)
