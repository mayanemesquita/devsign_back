from rest_framework import serializers

from devsign_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}
