from rest_framework import serializers
from booking.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    total_days = serializers.SerializerMethodField()
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['total_price']
        
    def validate_room_number(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Room Number must be greater than 0"
            )
        return value

    def validate(self, data):
        check_in = data.get('check_in_date')
        check_out = data.get('check_out_date')
        
        if check_out <= check_in:
            raise serializers.ValidationError(
                "check_out date must be after than the check_in date"
            )
        return data
    
    def get_total_days(self, obj):
        days = obj.check_out_date - obj.check_in_date
        return days.days