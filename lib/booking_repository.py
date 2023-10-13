from lib.booking import Booking
class BookingRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows:
            booking = Booking(row["id"], row["start_date"], row["end_date"], row["user_id"], row["space_id"])
            bookings.append(booking)
        return bookings
    
    def find_by_booking(self, booking_id):
        rows = self.connection.execute("SELECT * FROM bookings WHERE id=%s", [booking_id])
        row = rows[0]
        return Booking(row['id'], row["start_date"], row["end_date"], row["user_id"], row["space_id"])
    
    def find_by_space(self, space_id):
        rows = self.connection.execute("SELECT * FROM bookings WHERE space_id=%s", [space_id])
        row = rows[0]
        return Booking(row['id'], row["start_date"], row["end_date"], row["user_id"], row["space_id"])
    
    def find_by_user(self, user_id):
        rows = self.connection.execute("SELECT * FROM bookings WHERE user_id=%s", [user_id])
        bookings = [Booking(row['id'], row["start_date"], row["end_date"], row["user_id"], row["space_id"]) for row in rows]
        return bookings
    
    def create(self, booking):
        record = self.connection.execute("INSERT INTO bookings(start_date, end_date, user_id, space_id) VALUES(%s, %s, %s, %s) RETURNING id", [booking.start_date, booking.end_date, booking.user_id, booking.space_id])
        return record[0]['id']