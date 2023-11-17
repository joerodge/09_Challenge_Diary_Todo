from lib.todo import *

def test_init_of_Todo_obj():
    todo = Todo()
    assert todo.text == ''