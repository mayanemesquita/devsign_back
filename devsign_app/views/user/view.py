from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from devsign_app.models import User
from devsign_app.serializers import UserSerializer


class UserAPIViewController(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        result = User.objects.all()
        serializer = UserSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
