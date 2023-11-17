from lib.diary import *

# Test .add_contact()
def test_adding_contact_to_diary():
    diary = Diary()
    diary.add_contact("John Doe", "07123123123")
    assert diary.contacts == {"John Doe": "07123123123"}


def test_adding_multiple_contact_to_diary():
    diary = Diary()
    diary.add_contact("John Doe", "07123123123")
    diary.add_contact("Joe Bloggs", "07999999999")
    assert diary.contacts == {
        "John Doe": "07123123123",
        "Joe Bloggs": "07999999999",
        }



# Test .get_contacts()

def test_get_contacts():
    diary = Diary()
    diary.add_contact("John Doe", "07123123123")
    diary.add_contact("Joe Bloggs", "07999999999")
    diary.add_contact("Jane Doe", "07000000000")
    assert diary.get_contacts() == "John Doe: 07123123123\nJoe Bloggs: 07999999999\nJane Doe: 07000000000"