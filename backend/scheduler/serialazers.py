from .models import User, Company
from rest_framework import serializers

class UsersSerialazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CompanySerialazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name']