import sqlite3
from typing import List, Tuple


class Database:

    def __init__(self):
        self.connection = sqlite3.Connection("chinook.db")

    def get_tracks(self) -> List[Tuple]:
        result = []
        for row in self.connection.execute("""
                select TrackId, Name, Milliseconds, UnitPrice 
                    from tracks"""):
            result.append(row)
        return result

    def get_tracks_by_keyword(self, keyword):
        result = []
        for row in self.connection.execute(
                f"""select TrackId, Name, Milliseconds, UnitPrice
                        from tracks 
                        where Name like '%{keyword}%'"""):
            result.append(row)
        return result

    def insert_track(self, name: str, milliseconds: int, unitprice: float):
        with self.connection:
            self.connection.execute(
                f"""insert into tracks (Name, MediaTypeId, Milliseconds, UnitPrice)
                        values ('{name}', 1, {milliseconds}, {unitprice})""")

    def delete_track(self, name):
        with self.connection:
            self.connection.execute(
                f"""delete from tracks
                        where Name = '{name}'""")

    def update_track(self, name: str, milliseconds: int, unitprice: float):
        with self.connection:
            self.connection.execute(
                f"""update tracks 
                        set Milliseconds={milliseconds}, UnitPrice={unitprice}
                        where Name='{name}'""")

    def get_artists(self) -> List[Tuple]:
        result = []
        for row in self.connection.execute(
                f"""select artistID, Name from artists"""):
            result.append(row)
        return result

    def get_artists_by_keyword(self, name: str) -> List[Tuple]:
        result = []
        for row in self.connection.execute(
                f"""select artistID, Name from artists
                        where Name like '%{name}%'"""):
            result.append(row)
        return result

    def insert_artist(self, name):
        with self.connection:
            self.connection.execute(
                f"""insert into artists (Name)
                        values ('{name}')""")

    def delete_artist(self, name):
        with self.connection:
            self.connection.execute(
                f"""delete from artists
                        where name='{name}'""")

    def update_artist(self, old_name, new_name):
        with self.connection:
            self.connection.execute(
                f"""update artists
                        set Name='{new_name}'
                        where Name='{old_name}'""")

    def __del__(self):
        self.connection.close()
