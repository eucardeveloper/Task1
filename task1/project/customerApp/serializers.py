from rest_framework import serializers
from .models import CustomerAppModel

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAppModel 
        fields = ['pk', 'name', 'email', 'created']