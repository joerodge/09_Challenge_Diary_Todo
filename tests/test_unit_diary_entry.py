from lib.diary import *
import pytest

# Test __init__

def test_diary_entry_init():
    entry = DiaryEntry('Day1', 'Went for a walk')
    assert entry.title == 'Day1'
    assert entry.contents == 'Went for a walk'



## Test .count_words()

def test_count_words():
    entry = DiaryEntry('Day1', 'Went for a walk')
    assert entry.count_words() == 4

def test_count_words_zero():
    entry = DiaryEntry('Day1', '')
    assert entry.count_words() == 0



## Test .reading_time()

def test_reading_time():
    entry = DiaryEntry('Day1', 'Went for a short walk today')
    # 3 words per min for 6 words should be 2 mins
    assert entry.reading_time(3) == 2

def test_reading_time_2():
    entry = DiaryEntry('Day1', 'Went for a short walk today, it was really nice')
    # 5 words per min for 10 words should be 2 mins
    assert entry.reading_time(5) == 2

def test_reading_time_for_fractional_min_should_round_up():
    entry = DiaryEntry('Day1', 'Went for a short walk today, it was really nice')
    # 10 words / 4 wpm would be 2.5 test it rounds up
    assert entry.reading_time(4) == 3

def test_reading_time_with_0_wpm_is_error():
    entry = DiaryEntry('Day1', 'Went for a short walk today, it was really nice')
    with pytest.raises(Exception) as e:
        entry.reading_time(0) == 3
    assert str(e.value) == "WPM must be greater than 0"



## Test .reading_chunk()

def test_reading_chunk_read_all_text_if_wpm_high_enough_to_read_all_text():
    entry = DiaryEntry('Day1', 'Went for a short walk today, it was really nice')
    # should read 200 words in 2 mins at 100 wpm so should return 
    # all text as there are only 10 words
    assert entry.reading_chunk(100, 2) == 'Went for a short walk today, it was really nice'

def test_reading_chunk_only_returns_part_of_text():
    entry = DiaryEntry('Day1', 'Went for a short walk today, it was really nice')
    assert entry.reading_chunk(5, 1) == 'Went for a short walk'

def test_reading_chunk_twice_continues_where_last_chunk_ended():
    entry = DiaryEntry('Day1', 'Went for a short walk today, it was really nice')
    entry.reading_chunk(5, 1)
    assert entry.reading_chunk(5, 1) == 'today, it was really nice'

def test_reading_past_end_starts_reading_at_start_again():
    entry = DiaryEntry('Day1', 'Went for a short walk today, it was really nice')
    entry.reading_chunk(5, 1)
    entry.reading_chunk(5, 1)
    assert entry.reading_chunk(5, 1) == 'Went for a short walk'

def test_returns_empty_string_if_mins_or_wpm_is_zero():
    entry = DiaryEntry('Day1', 'Went for a short walk today, it was really nice')
    assert entry.reading_chunk(0, 0) == ''
