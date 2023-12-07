from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'age', 'consent_choice')
        #extra_kwargs = {'password': {'write_only': True, 'required': True}}

        
