from lib.diary import *
from lib.todo import *

def test_add_todo_list_to_diary():
    diary = Diary()
    assert diary.todo_list == None
    todo_list1 = TodoList()
    todo1 = Todo("Walk the dog")
    todo_list1.add(todo1)
    diary.add_todo_list(todo_list1)
    assert diary.todo_list == todo_list1


def test_adding_todo_to_a_todo_list_inside_a_diary():
    diary = Diary()
    todo_list1 = TodoList()
    diary.add_todo_list(todo_list1)
    todo1 = Todo("Walk the dog")
    diary.todo_list.add(todo1)
    assert diary.todo_list.incomplete() == [todo1]