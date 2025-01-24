from django.shortcuts import render
from rest_framework import viewsets

from bookmyshow.serializers import CreateBookSerializerRequest, CreateBookSerializerResponse


# Create your views here.

class BookingViewSet(viewsets.ViewSet):
    def __init__(self, bookingService, **kwargs):
        self.bookingService = bookingService
        super().__init__(**kwargs)

    def create_booking(self, request):
        try:
            req = CreateBookSerializerRequest(request.data)
            booking= self.bookingService.create_booking(
                user_id = request.data.get('user_id'),
                show_seat_ids = request.data.get('show_seat_ids'),
                show_id = request.data.get('show_id')
            )

            data = {
                "booking_id": booking.id,
                "response_status": booking.booking_status,
            }

            resp = CreateBookSerializerResponse(data=data)
            resp.is_valid(raise_exception=True)
            return resp.data

        except Exception as e:
            raise e


