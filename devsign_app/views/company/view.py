from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from devsign_app.models import Company
from devsign_app.serializers.company.serializer import CompanySerializer


class CompanyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        result = Company.objects.all()
        serializer = CompanySerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
