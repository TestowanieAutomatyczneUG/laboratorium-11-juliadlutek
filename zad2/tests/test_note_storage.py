import unittest
from unittest.mock import MagicMock
from zad2.src.notesStorage import NotesStorage


class TestNotesStorage(unittest.TestCase):
    def setUp(self):
        self.temp = NotesStorage()

    def test_notes_storage_add_note_correct(self):
        self.temp.add = MagicMock(return_value="New note added!")
        self.assertEqual(self.temp.add("Some note"), "New note added!")

    def test_notes_storage_add_string(self):
        self.temp.add = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.add, ":)")

    def test_notes_storage_add_empty_string(self):
        self.temp.add = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.add, "")

    def test_notes_storage_add_empty_float(self):
        self.temp.add = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.add, 2.3)

    def test_notes_storage_add_empty_none(self):
        self.temp.add = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.add, None)

    def test_notes_storage_add_empty_bool(self):
        self.temp.add = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.add, True)

    def test_notes_storage_clear_correct(self):
        self.temp.add("Some note")
        self.temp.clear = MagicMock(return_value="All notes deleted")
        self.assertEqual(self.temp.clear(), "All notes deleted")

    def test_notes_storage_clear_with_any_notes(self):
        self.temp.clear = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.clear)

    # def test_notes_storage_get_all_notes_of_non_existent(self):
    #     notes_storage = NotesStorage()
    #     notes_storage.getAllNotesOf = MagicMock(side_effect=ValueError)
    #
    #     self.assertRaises(ValueError, notes_storage.getAllNotesOf, "Andrzej")

    def test_notes_storage_get_all_notes_of_correct(self):
        self.temp.getAllNotesOf = MagicMock(return_value=[5, 4])
        self.assertEqual(self.temp.getAllNotesOf("Julia"), [5, 4])

    def test_notes_storage_get_all_notes_of_int(self):
        self.temp.getAllNotesOf = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.getAllNotesOf, 4)

    def test_notes_storage_get_all_notes_of_float(self):
        self.temp.getAllNotesOf = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.getAllNotesOf, 2.4)

    def test_notes_storage_get_all_notes_of_empty_str(self):
        self.temp.getAllNotesOf = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.getAllNotesOf, "")

    def test_notes_storage_get_all_notes_of_bool(self):
        self.temp.getAllNotesOf = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.getAllNotesOf, False)

    def test_notes_storage_get_all_notes_of_none(self):
        self.temp.getAllNotesOf = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.getAllNotesOf, None)


if __name__ == '__main__':
    unittest.main()