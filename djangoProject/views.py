from rest_framework.serializers import Serializer, IntegerField
from rest_framework.views import APIView


class BaseSerializer(Serializer):
    user_id = IntegerField()


class BaseAPIView(APIView):
    def initial(self, request, *args, **kwargs):
        if request.method == "GET":
            serializer = BaseSerializer(data=request.query_params)
            serializer.is_valid(raise_exception=True)
        else:
            serializer = BaseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

