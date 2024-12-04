from datetime import date
from main import Ticket


def test_fare():
    ticket = Ticket(fare=100, expiry_date=date(2024, 12, 1))
    assert isinstance(ticket.fare, int)
    assert ticket.fare == 100


def test_fare_zero():
    ticket = Ticket(fare=0, expiry_date=date(2024, 12, 1))
    assert ticket.fare == 0


def test_fare_error():
    ticket = Ticket(fare=bool, expiry_date=date(2024, 12, 1))


