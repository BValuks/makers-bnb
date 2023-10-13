from lib.space import *

class SpaceRepository:
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], 
                        row["description"], row["start_date"], 
                        row["end_date"], row["price"], row["user_id"])
            spaces.append(item)
        return spaces
    
    def find_by_space_id(self, id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row["id"], row["name"], 
                        row["description"], row["start_date"], 
                        row["end_date"], row["price"], row["user_id"])
        
    
    def find_by_user_id(self, user_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE user_id = %s', [user_id])
        spaces = [Space(row["id"], row["name"], 
                        row["description"], row["start_date"], 
                        row["end_date"], row["price"], row["user_id"]) for row in rows]
        return spaces
    
    def add_space(self, space):
        if space.end_date < space.start_date:
            raise Exception("End date cannot be earlier than start date")
        else: 
            self._connection.execute(
                'INSERT INTO spaces (name, description,start_date, end_date, price, user_id) VALUES (%s, %s, %s, %s, %s, %s)',
                [space.name, space.description, space.start_date, space.end_date, space.price, space.user_id]
                )
        return None