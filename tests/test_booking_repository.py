from lib.booking_repository import *
from lib.booking import *
import datetime
'''
When I put the connection name in it
it should save the connection
'''

def test_connection(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    assert repository.connection == db_connection
'''
When i use #get_all 
I should get all of the bookings
'''

def test_get_all(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    bookings = repository.all()
    assert bookings == [
        Booking(1, datetime.date(2030, 1, 17), datetime.date(2030, 1, 19), 2, 3),
        Booking(2, datetime.date(2031, 2, 10), datetime.date(2031, 2, 17), 1, 2),
        Booking(3, datetime.date(2030, 3, 4), datetime.date(2030, 3, 8), 2, 4),
        Booking(4, datetime.date(2030, 1, 25), datetime.date(2030, 2, 1), 1, 1)
        ]
    
'''
When we call booking by booking_id
we get the start time, end time, user_id and space_id for that booking Id
'''

def test_find_by_booking_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    bookings = repository.find_by_booking(1)
    assert bookings == Booking(1, datetime.date(2030, 1, 17), datetime.date(2030, 1, 19), 2, 3)

'''
When we call booking by space_id
we get the start time, end time, user_id and space_id for that booking Id
'''

def test_find_by_space_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    bookings = repository.find_by_space(3)
    assert bookings == Booking(1, datetime.date(2030, 1, 17), datetime.date(2030, 1, 19), 2, 3)

'''
when we call book repository #add
we add a new booking to the database
'''

def test_add_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    bookings = repository.create(Booking(None, datetime.date(2030, 4, 20), datetime.date(2030, 4, 25), 2, 3))
    assert bookings == 5
    assert repository.all() == [
        Booking(1, datetime.date(2030, 1, 17), datetime.date(2030, 1, 19), 2, 3),
        Booking(2, datetime.date(2031, 2, 10), datetime.date(2031, 2, 17), 1, 2),
        Booking(3, datetime.date(2030, 3, 4), datetime.date(2030, 3, 8), 2, 4),
        Booking(4, datetime.date(2030, 1, 25), datetime.date(2030, 2, 1), 1, 1),
        Booking(5, datetime.date(2030, 4, 20), datetime.date(2030, 4, 25), 2, 3)
    ]