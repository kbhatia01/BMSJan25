from rest_framework import serializers


class CreateBookSerializerRequest(serializers.Serializer):
    user_id = serializers.IntegerField()
    show_id = serializers.IntegerField()
    show_seat_ids = serializers.ListField(child=serializers.IntegerField())


class CreateBookSerializerResponse(serializers.Serializer):
    booking_id = serializers.IntegerField()
    response_status = serializers.CharField(max_length=100)
