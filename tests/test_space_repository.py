from lib.space_repository import *
from lib.space import *
import datetime
import pytest

'''
When we call SpaceRepository #all method
We get a list of Space objects reflecting the seed data
'''
def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [
        Space(1, 'space1', 'description1', datetime.date(2030,1,1), datetime.date(2030,2,1), 1000, 1),
        Space(2, 'space2', 'description2', datetime.date(2031,2,2), datetime.date(2031,2,28), 15000, 1), 
        Space(3, 'space3', 'description3', datetime.date(2030,1,15), datetime.date(2030,2,15), 2000, 2), 
        Space(4, 'space4', 'description4', datetime.date(2030,3,4), datetime.date(2030,3,14), 70000, 2)
    ]

'''
We can add a new space to the respository
And see it reflected in the list of all spaces
'''
def test_add_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    respository = SpaceRepository(db_connection)
    respository.add_space(Space(None, 'space5','description5', datetime.date(2030,4,1), datetime.date(2030,4,15), 3000, 2))
    result = respository.all()
    assert result == [
        Space(1, 'space1', 'description1', datetime.date(2030,1,1), datetime.date(2030,2,1), 1000, 1),
        Space(2, 'space2', 'description2', datetime.date(2031,2,2), datetime.date(2031,2,28), 15000, 1), 
        Space(3, 'space3', 'description3', datetime.date(2030,1,15), datetime.date(2030,2,15), 2000, 2), 
        Space(4, 'space4', 'description4', datetime.date(2030,3,4), datetime.date(2030,3,14), 70000, 2), 
        Space(5, 'space5','description5', datetime.date(2030,4,1), datetime.date(2030,4,15), 3000, 2)
    ]

'''
When we try to create a space object with end_date < start_date
We get an error
'''
def test_error_for_end_date_before_start_date(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    with pytest.raises(Exception) as e:
        result = repository.add_space(Space(
            None, 'space5','description5', datetime.date(2030,4,1), datetime.date(2030,3,15), 3000, 2
            ))
    error_message = str(e.value)
    assert error_message == "End date cannot be earlier than start date"
