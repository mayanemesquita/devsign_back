from rest_framework import generics

from devsign_app.models import Company
from devsign_app.serializers.company.serializer import CompanySerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
