from lib.todo import Todo

# Test fo __init__

def test_todo_onject_created():
    todo = Todo('Task1')
    assert todo.task == 'Task1'
    assert todo.completed == False



# Test .mark_complete()

def test_mark_complete_function_marks_completed_as_True():
    todo = Todo('Task1')
    todo.mark_complete()
    assert todo.completed == True