from rest_framework import serializers
from booking.models import Booking
from hotels.api.serializers import HotelsSerializer
class BookingSerializer(serializers.ModelSerializer):
    total_days = serializers.SerializerMethodField()
    hotel = HotelsSerializer(readoly= True)
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
    
    def create(self, validated_data):
        check_in = validated_data.get('check_in_date')
        check_out = validated_data.get('check_out_date')
        
        days = (check_out - check_in).days
        
        validated_data['total_price'] = days * 1000
        booking = Booking.objects.create(**validated_data)
        return booking
    
    def update(self, instance, validated_data):
        instance.hotel = validated_data.get(
            'hotel', 
            instance.hotel)
        
        instance.guest_name = validated_data.get(
            'guest_name',
            instance.guest_name
        )

        instance.email = validated_data.get(
            'email',
            instance.email
        )

        instance.room_number = validated_data.get(
            'room_number',
            instance.room_number
        )

        instance.check_in_date = validated_data.get(
            'check_in_date',
            instance.check_in_date
        )

        instance.check_out_date = validated_data.get(
            'check_out_date',
            instance.check_out_date
        )

        days = (
            instance.check_out_date -
            instance.check_in_date
        ).days
        
        instance.total_price = days * 1000
        instance.save()
        return instance