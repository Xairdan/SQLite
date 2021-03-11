from unittest import TestCase
import database


class TestDatabase(TestCase):
    def test_get_tracks(self):
        db = database.Database()
        tracks = db.get_tracks()
        print(len(tracks))

    def test_get_tracks_by_keyword(self):
        db = database.Database()
        tracks = db.get_tracks_by_keyword("wild")
        print(len(tracks))

    def test_insert_track(self):
        db = database.Database()
        db.insert_track("AAAAA", 200000, 2.99)
        tracks = db.get_tracks_by_keyword("AAAAA")
        print(tracks)
        db.delete_track("AAAAA")

    def test_delete_track(self):
        db = database.Database()
        db.delete_track("BBBBB")
        tracks = db.get_tracks_by_keyword("BBBBB")
        self.assertEqual(len(tracks), 0)
        db.insert_track("BBBBB", 200000, 1.99)
        tracks = db.get_tracks_by_keyword("BBBBB")
        self.assertEqual(len(tracks), 1)
        db.delete_track("BBBBB")
        tracks = db.get_tracks_by_keyword("BBBBB")
        self.assertEqual(len(tracks), 0)

    def test_update_track(self):
        db = database.Database()
        db.delete_track("CCCCC")
        tracks = db.get_tracks_by_keyword("CCCCC")
        self.assertEqual(len(tracks), 0)
        db.insert_track("CCCCC", 200000, 1.99)
        tracks = db.get_tracks_by_keyword("CCCCC")
        self.assertEqual(len(tracks), 1)
        db.update_track("CCCCC", 300000, 0.99)
        tracks = db.get_tracks_by_keyword("CCCCC")
        self.assertEqual(tracks[0][2], 300000)
        self.assertEqual(tracks[0][3], 0.99)
        db.delete_track("CCCCC")

    def test_get_artists(self):
        db = database.Database()
        artists = db.get_artists()
        print(len(artists))

    def test_get_artists_by_keyword(self):
        db = database.Database()
        artists = db.get_artists_by_keyword("A")
        print(len(artists))

    def test_insert_artist(self):
        db = database.Database()
        db.insert_artist("Todd Packer")
        artists = db.get_artists_by_keyword("Todd Packer")
        print(artists)
        db.delete_artist("Todd Packer")

    def test_delete_artist(self):
        db = database.Database()
        db.delete_artist("Todd Packer")
        artist = db.get_artists_by_keyword("Todd Packer")
        self.assertEqual(len(artist), 0)
        db.insert_artist("Todd Packer")
        artist = db.get_artists_by_keyword("Todd Packer")
        self.assertEqual(len(artist), 1)
        db.delete_artist("Todd Packer")
        artist = db.get_artists_by_keyword("Todd Packer")
        self.assertEqual(len(artist), 0)

    def test_update_artist(self):
        db = database.Database()
        db.delete_artist("Bob Packer")
        artist = db.get_artists_by_keyword("Bob Packer")
        self.assertEqual(len(artist), 0)
        db.insert_artist("Todd Packer")
        artist = db.get_artists_by_keyword("Todd Packer")
        self.assertEqual(len(artist), 1)
        db.update_artist("Todd Packer", "Bob Packer")
        artist = db.get_artists_by_keyword("Bob Packer")
        self.assertEqual(len(artist), 1)
        db.delete_artist("Bob Packer")
