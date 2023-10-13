```Python

class User:

    def __init__(self):  # NEED TO ADD ARGUMENTS
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        pass
        # gets all the user_data and returns it in a list of User instances

    def find_by_user_id(self, user_id):
        pass
        # returns the user according to the id, or None

    def find_by_user_email(self, user_name):
        pass
        # returns the user according to the username, or None

    def add_user(self, user):
        pass
        # checks if everything is valid
        # adds the users and returns the ID if all is valid, or False


class Space:

    def __init__(self):  # NEED TO ADD ARGUMENTS
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class SpaceRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        pass
        # gets all the space data and returns it in a list

    def find_by_space_id(self, space_id):
        pass
        # gets all the space data for the space that matches the id

    def find_by_user_id(self, user_id):
        pass
        # gets all the space data for the space that matches the user_id

    def add_space(self, space):
        pass
        # adds a space to the database


class Booking:

    def __init__(self):  # NEED TO ADD ARGUMENTS
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class BookingRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        pass
        # gets all the booking data and returns it in a list

    def find_by_booking_id(self, booking_id):
        pass
        # gets all the booking data for the booking that matches the id

    def find_by_space_id(self, space_id):
        pass
        # gets all the booking data for the booking that matches the space_id

    def add_booking(self, booking):
        pass
        # adds a booking to the database
