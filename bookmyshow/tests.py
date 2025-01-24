import time
from datetime import datetime
from unittest.mock import Mock

from django.utils import timezone

from django.test import TestCase

# Create your tests here.
from django.test import TransactionTestCase

from bookmyshow.models import User, Movie, Region, Theatre, Screen, Seat, SeatType, Feature, Show, ShowSeat, \
    showSeatStatus, ShowSeatType
from bookmyshow.service import BookShowService
from bookmyshow.views import BookingViewSet


class BookShowTestCase(TransactionTestCase):
    def setUp(self):
        self.user, val = User.objects.get_or_create(
            id=1,
            email='abc@gmail.com',
            password='password',
        )

        self.movie, val = Movie.objects.get_or_create(
            title="abc",
            release_date="2020-01-01",
            runtime=150
        )

        self.region, val = Region.objects.get_or_create(
            id=1,
            name="Delhi"
        )

        self.Theatre, val = Theatre.objects.get_or_create(
            name="PVR",
            region=self.region,
        )

        self.screen, val = Screen.objects.get_or_create(
            region=self.region,
            name="AUDI 1",
            theatre=self.Theatre,
        )

        self.seat1, val = Seat.objects.get_or_create(
            row_number=1,
            col_number=1,
            number="A1",
            seat_type=SeatType.SILVER,
            screen=self.screen
        )

        self.seat2, val = Seat.objects.get_or_create(
            row_number=1,
            col_number=2,
            number="A2",
            seat_type=SeatType.SILVER,
            screen=self.screen
        )

        self.features, val = Feature.objects.get_or_create(
            name="2D"
        )

        self.show, val = Show.objects.get_or_create(
            movie=self.movie,
            start_time=timezone.now() + timezone.timedelta(hours=1),
            end_time=timezone.now() + timezone.timedelta(hours=2),
            features=self.features,
            screen=self.screen,
        )

        self.show2, val = Show.objects.get_or_create(
            movie=self.movie,
            start_time=timezone.now() + timezone.timedelta(hours=3),
            end_time=timezone.now() + timezone.timedelta(hours=4),
            features=self.features,
            screen=self.screen,
        )

        self.showSeats, val = ShowSeat.objects.get_or_create(
            show=self.show,
            seat=self.seat1,
            show_seat_status=showSeatStatus.AVAILABLE
        )

        self.showSeats2, val = ShowSeat.objects.get_or_create(
            show=self.show,
            seat=self.seat2,
            show_seat_status=showSeatStatus.AVAILABLE
        )

        self.show2Seats, val = ShowSeat.objects.get_or_create(
            show=self.show2,
            seat=self.seat1,
            show_seat_status=showSeatStatus.AVAILABLE
        )

        self.show2Seats2, val = ShowSeat.objects.get_or_create(
            show=self.show2,
            seat=self.seat2,
            show_seat_status=showSeatStatus.AVAILABLE
        )

        self.showSeatTypes, val = ShowSeatType.objects.get_or_create(
            show=self.show,
            seat_type=SeatType.SILVER,
            price = 500
        )

        self.showSeatTypes2, val = ShowSeatType.objects.get_or_create(
            show=self.show2,
            seat_type=SeatType.SILVER,
            price = 300
        )

    def test_create_booking(self):
        self.service = BookShowService()
        self.view = BookingViewSet(bookingService=self.service)

        request_data = {
            'user_id': 1,
            'show_id': 1,
            'show_seat_ids': [2, 1]
        }

        request = Mock()
        request.data = request_data
        booking = self.view.create_booking(request)

        print(booking)

