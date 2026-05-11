from rest_framework import serializers
from hotels.models import Hotels

class HotelsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hotels
        field = '__all__'