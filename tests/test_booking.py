from lib.booking import Booking
'''
creating booking construct
'''

def test_construct():
    booking = Booking(1, "2030-01-17", "2030-01-19", 2, 3)
    assert booking.id == 1
    assert booking.start_date == "2030-01-17"
    assert booking.end_date == "2030-01-19"
    assert booking.user_id == 2
    assert booking.space_id == 3

'''
we need to check the value of the objects are same
'''
def test_bookings_are_equal():
    booking1 = Booking(1, "2030-01-17", "2030-01-19", 2, 3)
    booking2 = Booking(1, "2030-01-17", "2030-01-19", 2, 3)
    assert booking1 == booking2

'''
'''
def test_bookings_format():
    booking = Booking(1, "2030-01-17", "2030-01-19", 2, 3)
    assert str(booking) == "Booking(1, '2030-01-17', '2030-01-19', 2, 3)"
