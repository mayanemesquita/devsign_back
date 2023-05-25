from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from devsign_app.models import Company
from devsign_app.serializers.company.serializer import CompanySerializer


class CompanyAPIView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        result = Company.objects.all()
        serializer = CompanySerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyAPIViewDetails(APIView):

    @staticmethod
    def get(request, company_id, *args, **kwargs):
        result = Company.objects.get(company_id=company_id)
        serializer = CompanySerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, company_id, *args, **kwargs):
        result = Company.objects.get(company_id)
        serializer = CompanySerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, company_id, *args, **kwargs):
        result = Company.objects.get(company_id)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
