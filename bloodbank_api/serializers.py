from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import DonerDetails





class BankDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonerDetails
        fields = '__all__'
