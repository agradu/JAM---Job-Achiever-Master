from .models import User, Company
from rest_framework import serializers

<<<<<<< HEAD
class UsersSerialazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CompanySerialazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name']
=======

class ShedulerSerialazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sheduler
        fields = ["user", "application", "date"]
>>>>>>> 12b52f0 (Fix the bug in serializers and views)
