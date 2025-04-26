from rest_framework import serializers
from .models import Car, Customer, Booking
from django.db.models import Q

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        car = data['car']
        start_date = data['start_date']
        end_date = data['end_date']

        overlapping_bookings = Booking.objects.filter(
            car=car,
            start_date__lte=end_date,
            end_date__gte=start_date
        )
        if self.instance:
            overlapping_bookings = overlapping_bookings.exclude(id=self.instance.id)

        if overlapping_bookings.exists():
            raise serializers.ValidationError("Car is already booked for the selected dates!")

        return data
