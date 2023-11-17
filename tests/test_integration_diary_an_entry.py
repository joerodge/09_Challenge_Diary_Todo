from lib.diary import *
import pytest
# Test __init__()

def test_init_of_Diary():
    diary = Diary()
    assert diary.entries == []



# Test .add()

def test_add_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today')
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.entries == [entry1, entry2]


def test_add_something_other_than_DiaryEntry_does_nothing():
    diary = Diary()
    diary.add(12345)
    diary.add('hello')
    assert diary.entries == []



# Test .all()

def test_all_returns_list_of_all_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today')
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]


def test_all_when_no_DiaryEntry_added_yet_should_be_empty_list():
    diary = Diary()
    diary.all() == []



# Test .count_all_words()

def test_count_words_returns_correct_count_of_all_entries():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today')
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_all_words() == 14


def test_count_words_when_no_entries_added_is_0():
    diary = Diary()
    assert diary.count_all_words() == 0



# Test .reading_time()

def test_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today')
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog')
    diary.add(entry1)
    diary.add(entry2)
    # reading time of 14 words at 7 wpm should be 2 mins
    assert diary.reading_time(7) == 2

def test_reading_time2():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'hello '* 700)
    entry2 = DiaryEntry('Day2', 'goodbye '* 400)
    diary.add(entry1)
    diary.add(entry2)
    # 200 wpm to read 1100 = 5.5 min should return 6
    assert diary.reading_time(200) == 6


def test_reading_time_with_0_wpm_raises_error():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today')
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog')
    diary.add(entry1)
    diary.add(entry2)
    with pytest.raises(Exception) as e:
        diary.reading_time(0)
    assert str(e.value) == "WPM must be greater than 0"



# Test .find_best_entry_for_reading_time()

def test_find_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today.') #6
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog.') #8
    entry3 = DiaryEntry('Day3', 'Today I Babysat my nephews all day. Very tired now.') #10
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    # 9 wpm for 1 min can read 9 words so should return entry2 which is 8 words
    assert diary.find_best_entry_for_reading_time(9, 1) == entry2


def test_find_best_entry_for_reading_time_with_more_entries_and_longer_entries():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'testing ' * 150) 
    entry2 = DiaryEntry('Day2', 'testing ' * 225) 
    entry3 = DiaryEntry('Day3', 'testing ' * 320)
    entry4 = DiaryEntry('Day4', 'testing ' * 410)
    entry5 = DiaryEntry('Day5', 'testing ' * 500)
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.add(entry4)
    diary.add(entry5)
    # can read max 450 words in 3 mins at 150 wpm so should return 
    # entry 4 which is 410
    assert diary.find_best_entry_for_reading_time(150, 3) == entry4


def test_find_best_entry_for_reading_time_with_nothing_added_to_diary_returns_None():
    diary = Diary()
    assert diary.find_best_entry_for_reading_time(150, 3) == None


def test_find_best_entry_for_reading_time_no_suitible_diary_entry_returns_None():
    diary = Diary()
    entry1 = DiaryEntry('Day3', 'testing ' * 320)
    entry2 = DiaryEntry('Day4', 'testing ' * 410)
    entry3 = DiaryEntry('Day5', 'testing ' * 500)
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    # can only read 300 words in 2 mins at 150 wpm so their is no
    # entry that can be read as the smallest entry1 is 320 words
    assert diary.find_best_entry_for_reading_time(150, 2) == None


def test_find_best_entry_for_reading_time_mins_or_wpm_0():
    diary = Diary()
    entry1 = DiaryEntry('Day3', 'testing ' * 320)
    entry2 = DiaryEntry('Day4', 'testing ' * 410)
    entry3 = DiaryEntry('Day5', 'testing ' * 500)
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(0, 0) == None
    


# Test .read_next()

def test_read_next_one_entry():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today.')
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog.')
    entry3 = DiaryEntry('Day3', 'Today I Babysat my nephews all day. Very tired now.')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.read_next() == 'Day1: Went for a short walk today.'

def test_read_next_multiple_entries():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today.')
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog.')
    entry3 = DiaryEntry('Day3', 'Today I Babysat my nephews all day. Very tired now.')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.read_next()
    assert diary.read_next() == 'Day2: Went to the beach to walk the dog.'

def test_read_next_passed_the_end_should_start_from_the_start_again():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today.')
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog.')
    entry3 = DiaryEntry('Day3', 'Today I Babysat my nephews all day. Very tired now.')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.read_next()  #Day1
    diary.read_next()  #Day2
    diary.read_next()  #Day3
    # Then the next call should be Day1 again
    assert diary.read_next() == 'Day1: Went for a short walk today.'



# Test .read_all()

def test_read_all():
    diary = Diary()
    entry1 = DiaryEntry('Day1', 'Went for a short walk today.')
    entry2 = DiaryEntry('Day2', 'Went to the beach to walk the dog.')
    entry3 = DiaryEntry('Day3', 'Today I Babysat my nephews all day. Very tired now.')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.read_all() == 'Day1: Went for a short walk today.\nDay2: Went to the beach to walk the dog.\nDay3: Today I Babysat my nephews all day. Very tired now.'