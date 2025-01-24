import datetime
import threading
from datetime import timezone
import random

from bookmyshow.models import User, Show, ShowSeat, showSeatStatus, Ticket, BookingStatus


class BookShowService:

    def get_data(self, user_id, show_seats_id, show):
        user = User.objects.get(pk=user_id)
        show = Show.objects.get(pk=show)
        show_seats = ShowSeat.objects.filter(id__in=show_seats_id).order_by('seat_id')
        return user, show, show_seats

    def validate_booking(self, show_seats, show):

        #  show_seat_ids not more then 10
        if len(show_seats) > 10:
            raise OverflowError("seats length must be less than 10")
        # check if valid show..

        if show.start_time > datetime.datetime.now():
            raise Show.DoesNotExist

        #  check if seats exits and not booked

        for show_seat in show_seats:
            if show_seat.show_seat_status != showSeatStatus.AVAILABLE:
                raise ShowSeat.DoesNotExist

        return None

    def create_booking(self, user_id, show_seat_ids, show_id):

        user, show, show_seats = self.get_data(user_id, show_seat_ids, show_id)
        self.validate_booking(show_seats, show)

        # block seats..
        # lock
        for show_seat in show_seats:
            if show_seat.show_seat_status == showSeatStatus.AVAILABLE:
                show_seat.show_seat_status = showSeatStatus.LOCKED
                show_seat.save()
        # UNLOCK..
        # create a booking

        booking = Ticket(
            user=user,
            show=show,
            amount=100,
            booking_status=BookingStatus.IN_PROGRESS,
            ticket_number=random.randint(1, 999999),
        )
        # TODO: take payment against booking
        for show_seat in show_seats:
            show_seat.show_seat_status = showSeatStatus.RESERVED
            show_seat.save()
        booking.show_seats.set(show_seats)
        booking.booking_status = BookingStatus.BOOKED

        booking.save()
        return booking

        #  make seats reserved
        # change booking status
        # return booking..

# TODO:  CANCEL BOOKING
