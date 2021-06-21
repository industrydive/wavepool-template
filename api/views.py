from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import NewsPostSerializer
from news.models import NewsPost


class NewsPostApi(APIView):
    def get(self, request, *args, **kwargs):
        serializer = NewsPostSerializer(instance=NewsPost.objects.all(), many=True)
        response = serializer.data
        return Response(response)
