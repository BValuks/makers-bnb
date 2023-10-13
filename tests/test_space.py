from lib.space import *

def test_space_constructs():
    space = Space(1, 'space1', 'description1', '2030-01-01', '2030-02-01', '1000', 1)
    assert space.id == 1
    assert space.name == 'space1'
    assert space.description ==  'description1'
    assert space.start_date == '2030-01-01'
    assert space.end_date == '2030-02-01'
    assert space.price == '1000'
    assert space.user_id == 1

def test_compare_spaces():
    space1 = Space(1, 'space1', 'description1', '2030-01-01', '2030-02-01', '1000', 1)
    space2 = Space(1, 'space1', 'description1', '2030-01-01', '2030-02-01', '1000', 1)
    assert space1 == space2

'''
Spaces represented as strings
'''
def test_stringify_space_object():
    space = Space(1, 'space1', 'description1', '2030-01-01', '2030-02-01', '1000', 1)
    assert str(space) == 'Space(1, space1, description1, 2030-01-01, 2030-02-01, 1000, 1)'
