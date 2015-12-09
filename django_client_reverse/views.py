from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class Reverser(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        return Response("Response")
