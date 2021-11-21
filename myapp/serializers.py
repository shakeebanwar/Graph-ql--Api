from rest_framework import serializers
from django.contrib.auth.models import User
from django_restql.mixins import DynamicFieldsMixin





class UserSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields = '__all__'
