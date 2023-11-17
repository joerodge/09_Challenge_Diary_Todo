from lib.todo import *

# Test __init__

def test_init_of_TodoList_is_empty_list():
    todo_list = TodoList()
    assert todo_list.todos == []



# Test .add()

def test_add_a_Todo_to_TodoList():
    todo_list = TodoList()
    todo1 = Todo('Task1')
    todo2 = Todo('Task2')
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.todos == [todo1, todo2]


def test_add_type_other_than_todo_does_nothing():
    todo_list = TodoList()
    todo_list.add(3464)
    todo_list.add('hello')
    assert todo_list.todos == []



# Test .incomplete()

def test_incomplete():
    todo_list = TodoList()
    todo1 = Todo('Task1')
    todo2 = Todo('Task2')
    todo3 = Todo('Task3')
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo2.mark_complete()

    assert todo_list.incomplete() == [todo1, todo3]


def test_incomplete_returns_empty_list_when_no_todos_added():
    todo_list = TodoList()
    assert todo_list.incomplete() == []



# Test .complete()

def test_complete():
    todo_list = TodoList()
    todo1 = Todo('Task1')
    todo2 = Todo('Task2')
    todo3 = Todo('Task3')
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo2.mark_complete()

    assert todo_list.complete() == [todo2]


def test_complete_returns_empty_list_when_no_todos_added():
    todo_list = TodoList()
    assert todo_list.complete() == []



# Test .give_up()

def test_complete():
    todo_list = TodoList()
    todo1 = Todo('Task1')
    todo2 = Todo('Task2')
    todo3 = Todo('Task3')
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    assert [todo.completed for todo in todo_list.todos] == [False, False, False]
    todo_list.give_up()
    assert [todo.completed for todo in todo_list.todos] == [True, True, True]


def test_complete_when_no_todos_added_is_not_an_error():
    todo_list = TodoList()
    todo_list.give_up()
    assert todo_list.todos == []